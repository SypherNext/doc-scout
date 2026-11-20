import pandas as pd

df = pd.DataFrame({
    "model": ["gpt-4", "claude-3", "llama-3"],
    "accuracy": [0.94, 0.93, 0.89],
    "latency_ms": [1200, 1800, 900],
})

# Wrong: raises ValueError
df[(df["accuracy"] > 0.9) and (df["latency_ms"] < 1500)]

# Correct
df[(df["accuracy"] > 0.9) & (df["latency_ms"] < 1500)]
