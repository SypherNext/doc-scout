import pandas as pd

df = pd.DataFrame({
    "model": ["gpt-4", "claude-3", "llama-3", "gemini", "gpt-4"],
    "accuracy": [0.94, 0.93, 0.89, 0.91, 0.95],
    "latency_ms": [1200, 1800, 900, 1500, 1100],
})

# Boolean filter
high_acc = df[df["accuracy"] > 0.92]
print(high_acc)
#      model  accuracy  latency_ms
# 0    gpt-4      0.94        1200
# 1  claude-3      0.93        1800
# 4    gpt-4      0.95        1100

# Multiple conditions: use & (not and)
filtered = df[(df["accuracy"] > 0.9) & (df["latency_ms"] < 1500)]
print(filtered)
#    model  accuracy  latency_ms
# 0  gpt-4      0.94        1200
# 4  gpt-4      0.95        1100

# isin: filter by value set
gpt = df[df["model"].isin(["gpt-4", "gpt-3.5"])]
print(gpt)
#    model  accuracy  latency_ms
# 0  gpt-4      0.94        1200
# 4  gpt-4      0.95        1100

# Query method: string expression (cleaner for complex filters)
fast_accurate = df.query("accuracy > 0.9 and latency_ms < 1500")
print(fast_accurate)
