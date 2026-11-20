import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/llm_benchmarks.csv")
df["accuracy_per_dollar"] = df["accuracy"] / df["cost_per_1k_tokens"]
ranked = df.set_index("model_name")["accuracy_per_dollar"].sort_values(ascending=False)

fig, ax = plt.subplots(figsize=(8, 5))
ranked.plot(kind="bar", ax=ax, color="steelblue", edgecolor="black", title="Accuracy per Dollar by Model")
ax.set_ylabel("Accuracy per $1k-token cost")
ax.set_xlabel("")
ax.tick_params(axis="x", rotation=45)
ax.grid(True, axis="y", alpha=0.3)

plt.tight_layout()
fig.savefig("accuracy_per_dollar.png", dpi=150)
