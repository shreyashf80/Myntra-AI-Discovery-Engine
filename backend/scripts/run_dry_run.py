import asyncio
import sys
import os
import json

# Add the root of the project to PYTHONPATH so we can import src
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.shared.schemas import RawItem
from src.pipeline.extractor import Extractor

async def main():
    items = [
        RawItem(
            id="test:1",
            source="reddit",
            source_native_id="r1",
            query_tags=["Myntra help me decide"],
            content_type="post",
            title="Should I buy this on Myntra?",
            body="I have this dress in my wishlist for a wedding next month. I'm waiting for the EORS sale to drop the price, but I'm also really unsure about the fit because the reviews say it runs small. What do you guys think?",
            author="UserA",
            rating=5.0,
            timestamp="2023-01-01T00:00:00Z",
            url="",
            parent_id="",
            language_detected="en",
            language_original="en",
            ingested_at="2023-01-01T00:00:00Z"
        ),
        RawItem(
            id="test:2",
            source="app_store",
            source_native_id="a1",
            query_tags=["myntra app review"],
            content_type="review",
            title="App crashes",
            body="Every time I open my cart it crashes. Please fix.",
            author="UserB",
            rating=1.0,
            timestamp="2023-01-01T00:00:00Z",
            url="",
            parent_id="",
            language_detected="en",
            language_original="en",
            ingested_at="2023-01-01T00:00:00Z"
        )
    ]
    
    print("Running dry-run extraction on sample items...")
    tagged_items, discarded = await Extractor.process_batch(items)
    
    print(f"Discarded (irrelevant): {discarded}")
    print("Extracted Items:")
    for t in tagged_items:
        print(json.dumps(t.model_dump(), indent=2))

if __name__ == "__main__":
    asyncio.run(main())
