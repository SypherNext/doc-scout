import pandas as pd

df = pd.read_csv("data/llm_benchmarks.csv")

# Derive a provider column from the model name: a typical "clean" step
df["provider"] = df["model_name"].apply(
    lambda name: "Anthropic" if name.startswith("claude") else "OpenAI"
)

# Derived columns from existing ones
df["error_rate"] = 1 - df["accuracy"]
df["fast"] = df["latency_ms"] < 1000
df["accuracy_per_dollar"] = df["accuracy"] / df["cost_per_1k_tokens"]

# Group by provider
summary = df.groupby("provider").agg(
    avg_accuracy=("accuracy", "mean"),
    avg_latency=("latency_ms", "mean"),
    avg_cost=("cost_per_1k_tokens", "mean"),
    model_count=("model_name", "count"),
).reset_index()

summary["accuracy_rank"] = summary["avg_accuracy"].rank(ascending=False)
print(summary.sort_values("accuracy_rank"))
#     provider  avg_accuracy  avg_latency  avg_cost  model_count  accuracy_rank
# 0  Anthropic      0.898667       1640.0  0.006267            3            1.0
# 1     OpenAI      0.890400       1704.0  0.006320            5            2.0

# Which model gives the most accuracy per dollar?
best_value = df.loc[df["accuracy_per_dollar"].idxmax()]
print(best_value[["model_name", "accuracy", "cost_per_1k_tokens", "accuracy_per_dollar"]])
# model_name              gpt-4o-mini
# accuracy                      0.849
# cost_per_1k_tokens           0.0006
# accuracy_per_dollar          1415.0

print(df.sort_values("accuracy_per_dollar", ascending=False)[["model_name", "accuracy_per_dollar"]])
