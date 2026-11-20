import pandas as pd

df = pd.DataFrame({
    "model": ["gpt-4", "claude-3", "llama-3", "gemini", "gpt-4"],
    "accuracy": [0.94, 0.93, 0.89, 0.91, 0.95],
    "latency_ms": [1200, 1800, 900, 1500, 1100],
})

# Select columns by label
print(df["model"])          # Series
print(df[["model", "accuracy"]])  # DataFrame: note double brackets

# Select rows by position: iloc
print(df.iloc[0])           # First row as Series
print(df.iloc[1:3])         # Rows 1 and 2

# Select rows by label: loc
print(df.loc[0])            # Row with index label 0
print(df.loc[0:2])          # Rows 0 through 2 (inclusive: unlike iloc!)

# Select specific rows and columns with loc
print(df.loc[0:2, ["model", "accuracy"]])
#      model  accuracy
# 0    gpt-4      0.94
# 1  claude-3      0.93
# 2   llama-3      0.89
