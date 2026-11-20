# batch_predictor.py: Simulates collecting model predictions

import hashlib

def mock_predict(text):
    """Simulate a model prediction with a score."""
    # In reality, this would call an API.
    # Note: the built-in hash() is NOT a safe choice here. Python randomizes
    # the hash of strings on every process run (to prevent hash-flooding
    # attacks), so hash("same text") returns a different number each time
    # you run the script, even though it stays constant within one run.
    # hashlib.sha256 is a real, documented hash function: the same input
    # always produces the same digest, on any run, on any machine.
    digest = hashlib.sha256(text.encode("utf-8")).hexdigest()
    score = int(digest[:8], 16) % 100 / 100.0  # reproducible "score"
    return {"text": text, "score": score, "label": "positive" if score > 0.5 else "negative"}

inputs = [
    "Great product, highly recommend",
    "Not what I expected",
    "Works well for the price",
    "Terrible customer support",
    "Would buy again",
]

# Collect predictions
predictions = []
for text in inputs:
    predictions.append(mock_predict(text))

# Filter high-confidence predictions
high_conf = [p for p in predictions if p["score"] > 0.6]
print(f"Total predictions: {len(predictions)}")
print(f"High confidence: {len(high_conf)}")

# Extract just the labels
labels = [p["label"] for p in predictions]
print(f"Labels: {labels}")

# Count positives
positive_count = labels.count("positive")
print(f"Positive: {positive_count} / {len(labels)}")
