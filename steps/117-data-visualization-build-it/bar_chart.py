import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv("data/llm_benchmarks.csv")
models = df["model_name"]
accuracy = df["accuracy"]
latency = df["latency_ms"]

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 4))

# Accuracy bar chart: highlight the most accurate model
colors = ["coral" if a == accuracy.max() else "steelblue" for a in accuracy]
bars = ax1.bar(models, accuracy, color=colors, edgecolor="black")
ax1.set_ylabel("Accuracy")
ax1.set_title("Model Accuracy")
ax1.set_ylim(0, 1.0)
ax1.tick_params(axis="x", rotation=45)

# Add value labels on bars
for bar in bars:
    height = bar.get_height()
    ax1.text(bar.get_x() + bar.get_width()/2., height + 0.01,
             f"{height:.2f}", ha="center", va="bottom", fontsize=8)

# Latency bar chart
bars2 = ax2.bar(models, latency, color="lightcoral", edgecolor="black")
ax2.set_ylabel("Latency (ms)")
ax2.set_title("Inference Latency")
ax2.tick_params(axis="x", rotation=45)

for bar in bars2:
    h = bar.get_height()
    ax2.text(bar.get_x() + bar.get_width()/2., h + 20,
             f"{h:.0f}", ha="center", va="bottom", fontsize=8)

plt.tight_layout()
fig.savefig("model_comparison.png", dpi=150)
