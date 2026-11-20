# evaluation.py
"""Module for computing evaluation metrics."""

def accuracy(predictions, labels):
    """Calculate accuracy as fraction of correct predictions."""
    if len(predictions) != len(labels):
        raise ValueError("Predictions and labels must have the same length")
    correct = sum(1 for p, l in zip(predictions, labels) if p == l)
    return correct / len(predictions) if len(predictions) > 0 else 0.0

if __name__ == "__main__":
    preds = ["positive", "negative", "positive"]
    labels = ["positive", "positive", "positive"]
    acc = accuracy(preds, labels)
    print(f"Accuracy: {acc}")  # 2/3 = 0.667
