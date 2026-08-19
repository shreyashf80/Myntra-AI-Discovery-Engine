CORE_CATEGORIES = frozenset([
    "Men's Apparel", 
    "Women's Apparel", 
    "Kids' Apparel", 
    "Footwear"
])

EXPLORATORY_CATEGORIES = frozenset([
    "Accessories", 
    "Beauty & Personal Care", 
    "Jewelry",
    "Home & Living"
])

def classify_category_tier(category: str) -> str:
    """Returns 'core', 'exploratory', or 'unknown' for a given canonical category."""
    if category in CORE_CATEGORIES:
        return "core"
    if category in EXPLORATORY_CATEGORIES:
        return "exploratory"
    return "unknown"
