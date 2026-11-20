import csv
import numpy as np

def zscore_normalize(data):
    """Normalize data to mean=0, std=1 along each column."""
    data = np.asarray(data, dtype=np.float64)
    mean = data.mean(axis=0)
    std = data.std(axis=0)
    # Avoid division by zero for constant columns
    std = np.where(std == 0, 1.0, std)
    return (data - mean) / std

# Load the shared benchmark dataset: model_name, accuracy, latency_ms, cost_per_1k_tokens
with open("data/llm_benchmarks.csv", newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

names = np.array([r["model_name"] for r in rows])
features = np.array([
    [float(r["accuracy"]), float(r["latency_ms"]), float(r["cost_per_1k_tokens"])]
    for r in rows
])

normalized = zscore_normalize(features)
print("Original mean (accuracy, latency_ms, cost_per_1k):", np.round(features.mean(axis=0), 4))
# [   0.8935 1680.       0.0063]
print("Normalized mean:", np.round(normalized.mean(axis=0), 10))
# [-0.  0. -0.]: within floating-point precision
print("Normalized std:", np.round(normalized.std(axis=0), 2))
# [1. 1. 1.]

# Combine boolean masks across columns: above-average accuracy, below-average cost
efficient = names[(features[:, 0] > features[:, 0].mean()) & (features[:, 2] < features[:, 2].mean())]
print("Above-average accuracy, below-average cost:", efficient)
# ['claude-sonnet-4' 'gpt-4o']
