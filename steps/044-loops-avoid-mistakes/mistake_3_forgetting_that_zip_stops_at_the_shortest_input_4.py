models = ["gpt-4", "claude-3"]          # 2 items
scores = [0.95, 0.91, 0.87, 0.88]      # 4 items

for model, score in zip(models, scores):
    print(f"{model}: {score}")
# gpt-4: 0.95
# claude-3: 0.91
# The last 2 scores are silently ignored!
