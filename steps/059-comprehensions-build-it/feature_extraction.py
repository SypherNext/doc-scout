# feature_extraction.py

def extract_features(texts):
    """Extract word-level features from a list of text strings."""
    return {
        "word_counts": [len(t.split()) for t in texts],
        "avg_word_lengths": [
            sum(len(w) for w in t.split()) / max(len(t.split()), 1)
            for t in texts
        ],
        "unique_words_per_text": [
            len({w.lower() for w in t.split()})
            for t in texts
        ],
    }

texts = [
    "Transformer models process sequences of tokens",
    "Comprehensions make data transformation concise",
    "Attention",
]

features = extract_features(texts)
print("Word counts:", features["word_counts"])
print("Avg word lengths:", features["avg_word_lengths"])
print("Unique words:", features["unique_words_per_text"])
