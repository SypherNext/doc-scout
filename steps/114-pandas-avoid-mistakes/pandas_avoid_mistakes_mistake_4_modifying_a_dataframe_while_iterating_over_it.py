import pandas as pd

df = pd.DataFrame({
    "model": ["gpt-4", "claude-3", "llama-3"],
    "accuracy": [0.94, 0.93, 0.89],
})

# Slow and fragile: modifying while iterating
for idx, row in df.iterrows():
    if row["accuracy"] < 0.9:
        df.drop(idx, inplace=True)  # Modifies size during iteration


# Vectorized: fast and safe
df = df[df["accuracy"] >= 0.9]  # Filter instead of dropping in a loop

# Or collect indices first, then drop
drop_idx = df[df["accuracy"] < 0.9].index
df.drop(drop_idx, inplace=True)
