import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/llm_benchmarks.csv")
df["provider"] = df["model_name"].apply(
    lambda name: "Anthropic" if name.startswith("claude") else "OpenAI"
)
df["accuracy_per_dollar"] = df["accuracy"] / df["cost_per_1k_tokens"]

fig = plt.figure(figsize=(12, 8))
fig.suptitle("LLM Benchmark Dashboard", fontsize=16, fontweight="bold")

# 1. Accuracy by model
ax1 = fig.add_subplot(2, 2, 1)
colors = {"Anthropic": "#d97757", "OpenAI": "#1f9d55"}
bar_colors = [colors[p] for p in df["provider"]]
ax1.bar(df["model_name"], df["accuracy"], color=bar_colors, edgecolor="black")
ax1.set_ylabel("Accuracy")
ax1.set_title("Accuracy by Model")
ax1.set_ylim(0.8, 0.95)
ax1.tick_params(axis="x", rotation=45, labelsize=7)

# 2. Accuracy vs latency scatter
ax2 = fig.add_subplot(2, 2, 2)
for provider, group in df.groupby("provider"):
    ax2.scatter(group["latency_ms"], group["accuracy"], label=provider,
                color=colors[provider], alpha=0.8, edgecolors="black", s=70)
ax2.set_xlabel("Latency (ms)")
ax2.set_ylabel("Accuracy")
ax2.set_title("Accuracy vs Latency")
ax2.legend(fontsize=8)
ax2.grid(True, alpha=0.3)

# 3. Mean accuracy and cost by provider
ax3 = fig.add_subplot(2, 2, 3)
summary = df.groupby("provider").agg(
    avg_accuracy=("accuracy", "mean"), avg_cost=("cost_per_1k_tokens", "mean")
)
x = range(len(summary))
width = 0.35
ax3.bar([i - width/2 for i in x], summary["avg_accuracy"], width, label="Avg accuracy", color="steelblue")
ax3b = ax3.twinx()
ax3b.bar([i + width/2 for i in x], summary["avg_cost"], width, label="Avg cost", color="coral")
ax3.set_xticks(x)
ax3.set_xticklabels(summary.index)
ax3.set_ylabel("Avg accuracy")
ax3b.set_ylabel("Avg cost per 1k tokens ($)")
ax3.set_title("Mean Accuracy and Cost by Provider")

# 4. Accuracy-per-dollar ranking
ax4 = fig.add_subplot(2, 2, 4)
ranked = df.sort_values("accuracy_per_dollar")
ax4.barh(ranked["model_name"], ranked["accuracy_per_dollar"], color="steelblue", edgecolor="black")
ax4.set_title("Accuracy per Dollar (ranked)")
ax4.set_xlabel("Accuracy per $1k-token cost")
ax4.tick_params(axis="y", labelsize=7)

plt.tight_layout()
fig.savefig("dashboard.png", dpi=150)
print("Dashboard saved as dashboard.png")
