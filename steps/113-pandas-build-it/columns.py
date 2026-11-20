import pandas as pd

df = pd.DataFrame({
    "model": ["gpt-4", "claude-3", "llama-3"],
    "accuracy": [0.94, 0.93, 0.89],
    "latency_ms": [1200, 1800, 900],
})

# Create a new column from existing ones
df["error_rate"] = 1 - df["accuracy"]
print(df)
#      model  accuracy  latency_ms  error_rate
# 0    gpt-4      0.94        1200        0.06
# 1  claude-3      0.93        1800        0.07
# 2   llama-3      0.89         900        0.11

# Column with a condition: np.where
import numpy as np
df["fast"] = np.where(df["latency_ms"] < 1000, "yes", "no")

# Apply a function to a column
df["latency_s"] = df["latency_ms"] / 1000
print(df)
#      model  accuracy  latency_ms  error_rate fast  latency_s
# 0    gpt-4      0.94        1200        0.06   no       1.2
# 1  claude-3      0.93        1800        0.07   no       1.8
# 2   llama-3      0.89         900        0.11  yes       0.9
