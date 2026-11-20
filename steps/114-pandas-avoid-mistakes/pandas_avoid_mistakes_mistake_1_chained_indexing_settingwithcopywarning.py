import pandas as pd

df = pd.DataFrame({"model": ["gpt-4", "claude-3"], "accuracy": [0.94, 0.93]})

# Chained indexing: may modify a copy, not the original
subset = df[df["accuracy"] > 0.9]  # Returns a copy (usually)
subset["model"] = subset["model"].str.upper()
# SettingWithCopyWarning: A value is trying to be set on a copy of a slice


# Works: single assignment with .loc
df.loc[df["accuracy"] > 0.9, "model"] = df.loc[df["accuracy"] > 0.9, "model"].str.upper()

# Or be explicit about the copy
subset = df[df["accuracy"] > 0.9].copy()
subset["model"] = subset["model"].str.upper()
