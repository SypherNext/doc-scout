# data_dedup.py: Clean and filter dataset entries

def deduplicate_predictions(predictions, key_func=None):
    """Remove duplicate predictions based on a key function."""
    seen = set()
    unique = []

    for pred in predictions:
        if key_func is None:
            key = pred
        else:
            key = key_func(pred)

        if key not in seen:
            seen.add(key)
            unique.append(pred)

    return unique

# Simulated duplicate predictions
raw_predictions = [
    {"id": "001", "label": "positive", "text": "Great product"},
    {"id": "002", "label": "negative", "text": "Not good"},
    {"id": "001", "label": "positive", "text": "Great product"},  # Duplicate
    {"id": "003", "label": "neutral", "text": "It is okay"},
    {"id": "002", "label": "negative", "text": "Not good"},        # Duplicate
]

# Deduplicate by "id"
clean = deduplicate_predictions(raw_predictions, key_func=lambda p: p["id"])
print(f"Before: {len(raw_predictions)}, After: {len(clean)}")  # Before: 5, After: 3

# ---

# Fast stopword filtering using set membership
STOPWORDS = {"the", "a", "an", "is", "was", "are", "were",
             "in", "on", "at", "to", "for", "of", "and", "or", "it"}

def filter_stopwords(tokens):
    """Remove stopwords from a token list: O(n) total."""
    return [t for t in tokens if t.lower() not in STOPWORDS]

tokens = ["The", "cat", "is", "on", "the", "mat"]
filtered = filter_stopwords(tokens)
print(filtered)  # ['cat', 'mat']

# Without sets, this would be O(n * m) where m is the number of stopwords
# With sets, it is O(n): each check is O(1)
