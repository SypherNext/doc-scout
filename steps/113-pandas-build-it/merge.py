import pandas as pd

models = pd.DataFrame({
    "model_id": ["A1", "A2", "A3"],
    "model_name": ["gpt-4", "claude-3", "llama-3"],
    "provider": ["OpenAI", "Anthropic", "Meta"],
})

results = pd.DataFrame({
    "model_id": ["A1", "A1", "A2", "A3"],
    "accuracy": [0.94, 0.95, 0.93, 0.89],
})

# Merge: like SQL JOIN
merged = pd.merge(results, models, on="model_id", how="left")
print(merged)
#   model_id  accuracy model_name   provider
# 0       A1      0.94      gpt-4     OpenAI
# 1       A1      0.95      gpt-4     OpenAI
# 2       A2      0.93   claude-3  Anthropic
# 3       A3      0.89    llama-3       Meta

# Concatenate rows
more_results = pd.DataFrame({
    "model_id": ["A4"],
    "accuracy": [0.91],
})
combined = pd.concat([results, more_results], ignore_index=True)
print(combined)
#   model_id  accuracy
# 0       A1      0.94
# 1       A1      0.95
# 2       A2      0.93
# 3       A3      0.89
# 4       A4      0.91
