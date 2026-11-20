import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/llm_benchmarks.csv")

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 4))

ax1.hist(df["accuracy"], bins=5, alpha=0.7, color="steelblue", edgecolor="black")
ax1.set_xlabel("Accuracy")
ax1.set_ylabel("Number of models")
ax1.set_title("Accuracy Spread Across Models")

ax2.hist(df["cost_per_1k_tokens"], bins=5, alpha=0.7, color="coral", edgecolor="black")
ax2.set_xlabel("Cost per 1K tokens ($)")
ax2.set_ylabel("Number of models")
ax2.set_title("Cost Spread Across Models")

plt.tight_layout()
fig.savefig("histogram.png", dpi=150)
