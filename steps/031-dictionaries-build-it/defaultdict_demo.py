# defaultdict_demo.py
from collections import defaultdict

# Without defaultdict: you must check each time
word_counts = {}
words = ["apple", "banana", "apple", "cherry", "banana", "apple"]
for word in words:
    if word not in word_counts:
        word_counts[word] = 0
    word_counts[word] += 1

# With defaultdict: automatically provides default for missing keys
word_counts = defaultdict(int)  # int() returns 0
for word in words:
    word_counts[word] += 1

print(dict(word_counts))  # {'apple': 3, 'banana': 2, 'cherry': 1}

# Grouping items with defaultdict(list)
from collections import defaultdict

models_by_provider = defaultdict(list)
models_by_provider["OpenAI"].append("gpt-4")
models_by_provider["Anthropic"].append("claude-3")
models_by_provider["OpenAI"].append("gpt-3.5-turbo")

print(dict(models_by_provider))
# {'OpenAI': ['gpt-4', 'gpt-3.5-turbo'], 'Anthropic': ['claude-3']}
