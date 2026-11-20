import pandas as pd
import numpy as np

df = pd.DataFrame({
    "model": ["gpt-4", "claude-3", "llama-3", "gemini"],
    "accuracy": [0.94, None, 0.89, 0.91],
    "latency_ms": [1200, 1800, None, 1500],
})

print(df)
#      model  accuracy  latency_ms
# 0    gpt-4      0.94      1200.0
# 1  claude-3       NaN      1800.0
# 2   llama-3      0.89         NaN
# 3    gemini      0.91      1500.0

# Check for missing values
print(df.isna())
print(df.isna().sum())
# accuracy: 1, latency_ms: 1

# Drop rows with any missing values
clean = df.dropna()
print(clean)
#    model  accuracy  latency_ms
# 0  gpt-4      0.94      1200.0
# 3  gemini      0.91      1500.0

# Fill missing values
filled = df.fillna({"accuracy": df["accuracy"].mean(), "latency_ms": 0})
print(filled)
#      model  accuracy  latency_ms
# 0    gpt-4  0.940000      1200.0
# 1  claude-3  0.913333  ← mean of [0.94, 0.89, 0.91] = 0.9133
# 2   llama-3  0.890000         0.0  ← filled with 0
# 3    gemini  0.910000      1500.0
