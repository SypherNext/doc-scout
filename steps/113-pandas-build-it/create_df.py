import pandas as pd

# From a dict of lists
data = {
    "model": ["gpt-4", "claude-3", "llama-3", "gemini"],
    "accuracy": [0.94, 0.93, 0.89, 0.91],
    "latency_ms": [1200, 1800, 900, 1500],
}
df = pd.DataFrame(data)
print(df)
#      model  accuracy  latency_ms
# 0    gpt-4      0.94        1200
# 1  claude-3      0.93        1800
# 2   llama-3      0.89         900
# 3    gemini      0.91        1500

# From a list of dicts (one dict per row)
rows = [
    {"model": "gpt-4", "accuracy": 0.94},
    {"model": "claude-3", "accuracy": 0.93},
]
df2 = pd.DataFrame(rows)

# A Series is a single column
scores = pd.Series([0.94, 0.93, 0.89, 0.91], name="accuracy")
print(scores)
# 0    0.94
# 1    0.93
# 2    0.89
# 3    0.91
# Name: accuracy, dtype: float64

# From a CSV file, the most common way real data arrives:
# the shared data/llm_benchmarks.csv used across this course's data lessons
bench = pd.read_csv("data/llm_benchmarks.csv")
print(bench)
#         model_name  accuracy  latency_ms  cost_per_1k_tokens
# 0    claude-opus-4     0.927        2850              0.0150
# 1  claude-sonnet-4     0.908        1450              0.0030
# ...

# Basic inspection
print(df.shape)       # (4, 3)
print(df.columns)     # Index(['model', 'accuracy', 'latency_ms'], dtype='object')
print(df.dtypes)      # model: object, accuracy: float64, latency_ms: int64
print(bench.describe())  # Summary statistics for numeric columns
