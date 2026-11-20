# basic_if.py

def classify_sentiment(score):
    """Classify a sentiment score into a label."""
    if score is None:
        return "unknown"

    if score > 0.6:
        return "positive"
    elif score > 0.3:
        return "neutral"
    else:
        return "negative"

print(classify_sentiment(0.85))  # positive
print(classify_sentiment(0.45))  # neutral
print(classify_sentiment(0.15))  # negative
print(classify_sentiment(None))  # unknown
