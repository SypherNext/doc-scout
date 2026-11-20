# type_hints.py

def classify_text(
    text: str,
    threshold: float = 0.5,
    labels: list[str] | None = None,
) -> dict[str, float]:
    """
    Classify text and return a dict mapping labels to scores.

    Args:
        text: Input text to classify.
        threshold: Minimum confidence to include a label.
        labels: Specific labels to consider. If None, use all.

    Returns:
        Dict of label -> confidence score.
    """
    # Simulated classification
    scores = {
        "positive": 0.92,
        "negative": 0.03,
        "neutral": 0.05,
    }

    if labels:
        scores = {k: v for k, v in scores.items() if k in labels}

    return {k: v for k, v in scores.items() if v >= threshold}

result = classify_text("Great product!", threshold=0.5, labels=["positive"])
print(result)  # {'positive': 0.92}

# This shows the type annotation in IDEs and when you hover over the function
# It does NOT raise an error if you pass wrong types: that is what mypy is for
