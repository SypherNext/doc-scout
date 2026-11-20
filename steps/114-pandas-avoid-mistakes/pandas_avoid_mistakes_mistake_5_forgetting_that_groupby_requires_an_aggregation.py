import pandas as pd

df = pd.DataFrame({
    "model": ["gpt-4", "gpt-4", "claude-3"],
    "accuracy": [0.94, 0.95, 0.93],
})

# This returns a GroupBy object, not a DataFrame
grouped = df.groupby("model")
print(grouped)  # <pandas.core.groupby.DataFrameGroupBy object: not useful!

# You MUST call an aggregation
result = grouped["accuracy"].mean()
print(result)
# model
# claude-3    0.93
# gpt-4       0.945
