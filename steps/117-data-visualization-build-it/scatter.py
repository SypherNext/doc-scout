import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/llm_benchmarks.csv")
df["provider"] = df["model_name"].apply(
    lambda name: "Anthropic" if name.startswith("claude") else "OpenAI"
)

fig, ax = plt.subplots(figsize=(8, 5))

colors = {"Anthropic": "#d97757", "OpenAI": "#1f9d55"}
for provider, group in df.groupby("provider"):
    ax.scatter(group["latency_ms"], group["accuracy"],
               label=provider, color=colors[provider], alpha=0.8, edgecolors="black", s=80)
    for _, row in group.iterrows():
        ax.annotate(row["model_name"], (row["latency_ms"], row["accuracy"]),
                     textcoords="offset points", xytext=(6, 4), fontsize=7)

ax.set_xlabel("Latency (ms)")
ax.set_ylabel("Accuracy")
ax.set_title("Accuracy vs Latency by Provider")
ax.legend()
ax.grid(True, alpha=0.3)

fig.savefig("scatter.png", dpi=150)
