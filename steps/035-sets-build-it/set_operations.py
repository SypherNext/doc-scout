# set_operations.py
all_models = {"gpt-4", "claude-3", "llama-3", "gemini-pro"}
production_models = {"gpt-4", "claude-3"}

# Union: all elements from both sets
print(all_models | production_models)
# {'gpt-4', 'claude-3', 'llama-3', 'gemini-pro'}

# Intersection: elements in both sets
print(all_models & production_models)
# {'gpt-4', 'claude-3'}

# Difference: elements in first but not second
print(all_models - production_models)
# {'llama-3', 'gemini-pro'}

# Symmetric difference: elements in either but not both
a = {"cat", "dog"}
b = {"dog", "fox"}
print(a ^ b)  # {'cat', 'fox'}

# Subset / superset checks
small = {"gpt-4"}
print(small.issubset(all_models))        # True
print(all_models.issuperset(small))      # True
print(small.isdisjoint({"llama-3"}))     # True: no overlap
