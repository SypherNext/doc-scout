import pandas as pd

df = pd.DataFrame({
    "model": ["gpt-4", "gpt-4", "claude-3", "claude-3", "llama-3"],
    "dataset": ["v1", "v2", "v1", "v2", "v1"],
    "accuracy": [0.94, 0.95, 0.93, 0.92, 0.89],
    "latency_ms": [1200, 1100, 1800, 1700, 900],
})

# Group by model and compute mean
avg = df.groupby("model")["accuracy"].mean()
print(avg)
# model
# claude-3    0.925
# gpt-4       0.945
# llama-3     0.890
# Name: accuracy, dtype: float64

# Multiple aggregations
stats = df.groupby("model").agg({
    "accuracy": ["mean", "std"],
    "latency_ms": ["mean", "min", "max"],
})
print(stats)
#           accuracy          latency_ms
#               mean       std    mean  min   max
# model
# claude-3    0.925  0.007071  1750.0 1700  1800
# gpt-4       0.945  0.007071  1150.0 1100  1200
# llama-3     0.890       NaN   900.0  900   900

# Group by two columns
by_model_dataset = df.groupby(["model", "dataset"])["accuracy"].mean()
print(by_model_dataset)
# model     dataset
# claude-3  v1         0.93
#           v2         0.92
# gpt-4     v1         0.94
#           v2         0.95
# llama-3   v1         0.89
