# iteration.py
models = ["gpt-4", "claude-3", "llama-3", "gemini-pro"]

# Length
print(len(models))  # 4

# Basic for loop
for model in models:
    print(model)

# Loop with index using enumerate
for index, model in enumerate(models):
    print(f"{index}: {model}")
# 0: gpt-4
# 1: claude-3
# 2: llama-3
# 3: gemini-pro
