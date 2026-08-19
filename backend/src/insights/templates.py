from typing import List, Dict

class SeedQuestion:
    def __init__(self, id: str, text: str, expected_signals: List[str]):
        self.id = id
        self.text = text
        self.expected_signals = expected_signals

SEED_QUESTIONS: List[SeedQuestion] = [
    SeedQuestion(
        id="q1",
        text="Why did users save/wishlist the product? (Wishlist behaviour)",
        expected_signals=["genuine purchase consideration", "compare/shortlist", "waiting for sale", "event/occasion", "inspiration"]
    ),
    SeedQuestion(
        id="q2",
        text="What prevents them from purchasing and what uncertainty remains? (Decision friction)",
        expected_signals=["fit/size", "fabric/quality", "styling", "price/sale hesitation", "return-policy"]
    ),
    SeedQuestion(
        id="q3",
        text="Are they comparing alternatives and what happens after saving? (Decision process)",
        expected_signals=["comparison", "analysis paralysis", "myntra vs ajio"]
    ),
    SeedQuestion(
        id="q4",
        text="What information do they seek and where do they go? (External behaviour)",
        expected_signals=["Reddit", "YouTube", "Instagram", "friends", "offline store"]
    ),
    SeedQuestion(
        id="q5",
        text="Did they purchase, postpone, abandon, or buy an alternative? (Outcome)",
        expected_signals=["purchased", "purchased alternative", "postponed", "abandoned"]
    )
]
