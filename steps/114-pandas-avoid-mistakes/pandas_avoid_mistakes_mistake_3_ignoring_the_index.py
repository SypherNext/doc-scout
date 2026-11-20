import pandas as pd

df = pd.DataFrame({"accuracy": [0.94, 0.93, 0.89]}, index=["run1", "run2", "run3"])
# Filter
filtered = df[df["accuracy"] > 0.9]
print(filtered.index)  # Index(['run1', 'run2'], dtype='object')

# After operations, the index carries over
# When merging, index misalignment can cause NaN values
