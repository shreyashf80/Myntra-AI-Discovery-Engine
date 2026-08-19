import os
import logging
import datetime
from typing import List, Dict, Any
import urllib.parse
from apify_client import ApifyClient

from src.connectors.base import BaseConnector
from src.shared.schemas import RawItem

logger = logging.getLogger(__name__)

class RedditConnector(BaseConnector):
    def __init__(self):
        self.source_name = "reddit"
        
    def get_source_name(self) -> str:
        return self.source_name

    def _parse_timestamp(self, ts) -> str:
        if not ts:
            return datetime.datetime.now(datetime.timezone.utc).isoformat()
        if isinstance(ts, str) and "T" in ts:
            return ts
        if isinstance(ts, (int, float)):
            dt = datetime.datetime.fromtimestamp(ts, tz=datetime.timezone.utc)
            return dt.isoformat()
        try:
            dt = datetime.datetime.fromtimestamp(float(ts), tz=datetime.timezone.utc)
            return dt.isoformat()
        except ValueError:
            return str(ts)

    def normalize_item(self, post: Dict, query: str) -> RawItem:
        post_id = post.get("id", "")
        body = post.get("selftext") or post.get("body") or post.get("text") or ""
        title = post.get("title", "")
        
        url = post.get("url") or post.get("permalink", "")
        if url and not url.startswith("http"):
            url = f"https://reddit.com{url}"
            
        author = post.get("author", "")
        if isinstance(author, dict):
             author = author.get("name", "")

        return RawItem(
            id=f"reddit:{post_id}",
            source=self.source_name,
            source_native_id=post_id,
            query_tags=[query],
            content_type="post",
            title=title,
            body=body,
            author=author,
            rating=float(post.get("upvotes", 0) or post.get("score", 0) or 0),
            timestamp=self._parse_timestamp(post.get("createdAt") or post.get("created_utc")),
            url=url,
            parent_id=post.get("parent_id"),
            language_detected="",
            language_original="",
            ingested_at=datetime.datetime.now(datetime.timezone.utc).isoformat()
        )

    def get_intent_queries(self, config: Any) -> Dict[str, List[str]]:
        return {
            "wishlist_decisions": [
                "Myntra help me decide",
                "Myntra vs Ajio",
                "Myntra size fit",
                "Myntra wishlist",
                "worth buying from Myntra"
            ]
        }

    def get_default_subreddits(self, config: Any) -> List[str]:
        return [
            "IndianFashionAddicts", 
            "IndiaMFA", 
            "TwoXIndia", 
            "InstaCelebsGossip", 
            "IndianBeautyChatter"
        ]

    async def fetch(self, config: Any) -> List[RawItem]:
        from src.shared.config import config as app_config
        token = app_config.APIFY_API_TOKEN
        if not token:
            logger.error("APIFY_API_TOKEN is not set. Cannot run Reddit scraper.")
            return []
            
        client = ApifyClient(token)
        intent_queries = self.get_intent_queries(config)
        subreddits = self.get_default_subreddits(config)
        
        reddit_count = getattr(config, "reddit_count", 100)
        
        start_urls = []
        all_queries = []
        for intent, queries in intent_queries.items():
            all_queries.extend(queries)
            
        for sub in subreddits:
            for query in all_queries:
                q = urllib.parse.quote(query)
                start_urls.append({"url": f"https://www.reddit.com/r/{sub}/search/?q={q}&restrict_sr=1"})
                
        run_input = {
            "startUrls": start_urls,
            "searchSort": "relevance",
            "searchTime": "all",
            "maxPostsCount": reddit_count,
            "maxCommentsCount": 10
        }
        
        logger.info(f"Triggering harshmaur/reddit-scraper with {len(start_urls)} URLs. Max posts: {reddit_count}")
        try:
            import asyncio
            loop = asyncio.get_event_loop()
            run = await loop.run_in_executor(None, lambda: client.actor("harshmaur/reddit-scraper").call(run_input=run_input))
            
            logger.info("Scraper finished, fetching dataset...")
            dataset_id = run["defaultDatasetId"]
            dataset_items = await loop.run_in_executor(None, lambda: client.dataset(dataset_id).list_items().items)
            
        except Exception as e:
            logger.error(f"Apify Reddit Scraper failed: {e}")
            return []
            
        raw_items_map = {}
        for item in dataset_items:
            raw_item = self.normalize_item(item, "Myntra wishlist")
            if not raw_item.body and not raw_item.title:
                continue
            if raw_item.id not in raw_items_map:
                raw_items_map[raw_item.id] = raw_item
                
        return list(raw_items_map.values())
