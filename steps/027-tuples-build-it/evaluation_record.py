# evaluation_record.py: Store and process evaluation results

from datetime import datetime

# Each record is a tuple: (model_name, accuracy, f1_score, timestamp)
def evaluate_model(model_name):
    """Simulate evaluating a model and returning results."""
    # In reality, you would run actual evaluation
    accuracy = 0.85 + (hash(model_name) % 15) / 100.0
    f1 = accuracy - 0.03
    return (model_name, accuracy, f1, datetime.now())

# Collect evaluation records
models = ["gpt-4", "claude-3", "llama-3", "gemini-pro"]
results = [evaluate_model(m) for m in models]

# Unpack and print each record
for name, acc, f1, ts in results:
    print(f"{name}: acc={acc:.3f}, f1={f1:.3f}")

# Find the best model by accuracy
best = max(results, key=lambda r: r[1])
print(f"\nBest model: {best[0]} with accuracy {best[1]:.3f}")

# Use tuple as key in a cache
prediction_cache = {}

def cached_predict(model, prompt):
    key = (model, prompt)
    if key not in prediction_cache:
        # Simulate prediction
        prediction_cache[key] = ("positive", 0.95)
    return prediction_cache[key]
