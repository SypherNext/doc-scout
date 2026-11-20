# Ternary (modifies each element, keeps all)
[s if s > 0.5 else 0.0 for s in scores]

# Filter (removes elements entirely)
[s for s in scores if s > 0.5]
