import json
import logging
import asyncio
import datetime
from typing import List, Tuple, Dict
from src.shared.schemas import RawItem, TaggedItem
from src.shared.llm import llm_client

logger = logging.getLogger(__name__)

class Extractor:
    BATCH_SIZE = 25

    SYSTEM_PROMPT = """You are a qualitative research AI analyzing user feedback for Myntra (a fashion e-commerce app).
Your task is to structure the provided batch of reviews/comments against a specific research taxonomy focused on wishlist-to-purchase conversion.

OUTPUT FORMAT:
You must return a raw JSON array. DO NOT wrap it in markdown blockquotes like ```json.
[
  {
    "id": "review_id_1",
    "relevant": true/false,
    "category_mentioned": ["Men's Apparel", "Accessories", ...],
    "journey_stage": "pre-purchase" | "comparison" | "purchase" | "post-purchase" | "unknown",
    "wishlist_intent": ["genuine purchase consideration", "compare/shortlist", "waiting for sale", "event/occasion planning", "inspiration/moodboard", "unknown"],
    "primary_barrier": "fit/size" | "fabric/quality" | "styling" | "price/sale hesitation" | "return-policy concern" | "comparison/analysis paralysis" | "delivery/timing concern" | "other" | "unknown",
    "information_need": "free text or null (e.g. fit, size, styling, reviews)",
    "external_validation_sought": "Reddit" | "YouTube" | "Instagram" | "friends/family" | "Google" | "offline store" | "competitor platform" | "none" | "unknown",
    "workaround": "free text or null (what does the user currently do instead of getting the answer directly from the platform?)",
    "purchase_outcome": "purchased wishlisted item" | "purchased alternative" | "postponed" | "abandoned" | "unknown",
    "conversion_trigger": "event/occasion" | "social validation" | "low stock" | "price change" | "information/uncertainty resolved" | "recommendation" | "other" | "unknown",
    "wishlist_purchase_link": "direct" | "indirect" | "contextual" | "none",
    "sentiment": "positive" | "neutral" | "negative",
    "source_snippet": "exact quote from the review that justifies the tags"
  }
]

RULES:
1. Wishlist Intent can contain multiple values if evidence supports it.
2. DO NOT infer conversion triggers or purchase outcomes when the source does not explicitly state one. Use "unknown".
3. Clearly separate users discussing products before purchase (pre-purchase/consideration) from people reviewing products they already bought (post-purchase).
4. Objectively capture price/sale behaviour if present, do not filter it out.
5. If the item is generic noise, spam, or a pure technical bug with no shopping/wishlist/consideration signal, set "relevant": false and you can leave other fields null.
6. Ensure the `id` perfectly matches the id provided in the input batch.
"""

    @classmethod
    def _categorize_tier(cls, cats: List[str]) -> List[str]:
        from src.shared.taxonomy import classify_category_tier
        tiers = set()
        for c in cats:
            t = classify_category_tier(c)
            if t != "unknown":
                tiers.add(t)
        return list(tiers) if tiers else ["not stated"]

    @classmethod
    async def process_batch(cls, batch: List[RawItem]) -> Tuple[List[TaggedItem], int]:
        input_data = []
        for item in batch:
            input_data.append({
                "id": item.id,
                "text": f"{(item.title + ' | ') if item.title else ''}{item.body}"
            })
            
        user_prompt = "Batch to process:\n" + json.dumps(input_data, indent=2)
        
        try:
            response = await llm_client.complete(system=cls.SYSTEM_PROMPT, user=user_prompt)
            # Clean possible markdown
            content = response.content.strip()
            if content.startswith("```json"): content = content[7:]
            if content.startswith("```"): content = content[3:]
            if content.endswith("```"): content = content[:-3]
            
            extracted_array = json.loads(content)
            
            tagged_items = []
            discarded = 0
            
            for ext in extracted_array:
                if not ext.get("relevant", False):
                    discarded += 1
                    continue
                    
                # Find matching original item
                original = next((i for i in batch if i.id == ext["id"]), None)
                if not original:
                    continue
                    
                cat_mentioned = ext.get("category_mentioned", ["not stated"])
                if not isinstance(cat_mentioned, list):
                    cat_mentioned = [cat_mentioned] if cat_mentioned else ["not stated"]
                    
                frustration = ext.get("frustration") or {}
                if isinstance(frustration, str):
                    frustration = {"summary": frustration, "severity": "med"}
                    
                tagged = TaggedItem(
                    id=original.id,
                    source=original.source,
                    category_mentioned=cat_mentioned,
                    category_tier=cls._categorize_tier(cat_mentioned),
                    journey_stage=ext.get("journey_stage", "unknown"),
                    wishlist_intent=ext.get("wishlist_intent", ["unknown"]) if isinstance(ext.get("wishlist_intent"), list) else [ext.get("wishlist_intent", "unknown")],
                    primary_barrier=ext.get("primary_barrier", "unknown"),
                    information_need=ext.get("information_need", "unknown") or "unknown",
                    external_validation_sought=ext.get("external_validation_sought", "unknown"),
                    workaround=ext.get("workaround", "unknown") or "unknown",
                    purchase_outcome=ext.get("purchase_outcome", "unknown"),
                    conversion_trigger=ext.get("conversion_trigger", "unknown"),
                    wishlist_purchase_link=ext.get("wishlist_purchase_link", "none"),
                    sentiment=ext.get("sentiment", "neutral"),
                    source_snippet=ext.get("source_snippet", ""),
                    body=original.body,
                    timestamp=original.timestamp,
                    rating=original.rating,
                    url=original.url,
                    extraction_model=response.llm_used,
                    extracted_at=datetime.datetime.now(datetime.timezone.utc).isoformat()
                )
                tagged_items.append(tagged)
                
            return tagged_items, discarded
            
        except Exception as e:
            logger.error(f"Failed to process batch: {e}")
            return [], len(batch) # Treat all as discarded on total failure

    @classmethod
    async def extract_all(cls, items: List[RawItem]) -> Tuple[List[TaggedItem], int]:
        all_tagged = []
        total_discarded = 0
        
        # Process in batches
        for i in range(0, len(items), cls.BATCH_SIZE):
            batch = items[i:i + cls.BATCH_SIZE]
            logger.info(f"Extracting batch {i//cls.BATCH_SIZE + 1}/{(len(items) + cls.BATCH_SIZE - 1)//cls.BATCH_SIZE} ({len(batch)} items)...")
            
            tagged, discarded = await cls.process_batch(batch)
            all_tagged.extend(tagged)
            total_discarded += discarded
            
            # Throttle to respect LLM rate limits (Gemini is 15 RPM, so 4 seconds per request)
            if i + cls.BATCH_SIZE < len(items):
                await asyncio.sleep(4.1) 
                
        return all_tagged, total_discarded
