# lambda_demo.py

# Lambda: lambda arguments: expression
square = lambda x: x ** 2
print(square(5))  # 25

# Using lambda with sorted: sort models by length
models = ["gpt-4", "claude-3-opus", "llama-3", "gemini-pro"]
sorted_models = sorted(models, key=lambda m: len(m))
print(sorted_models)  # ['gpt-4', 'llama-3', 'gemini-pro', 'claude-3-opus']

# Using lambda with filter: keep only short prompts
prompts = ["Tell me a joke", "Hi", "Explain quantum computing in detail"]
short_prompts = list(filter(lambda p: len(p) < 20, prompts))
print(short_prompts)  # ['Tell me a joke', 'Hi']

# Using lambda with map: add prefix
with_prefix = list(map(lambda p: "Q: " + p, prompts))
print(with_prefix)
# ['Q: Tell me a joke', 'Q: Hi', 'Q: Explain quantum computing in detail']
