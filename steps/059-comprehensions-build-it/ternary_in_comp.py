# ternary_in_comp.py
scores = [0.92, 0.45, 0.88, 0.32, 0.95]

# Ternary in expression position: modifies every element, keeps all
processed = [s if s > 0.5 else 0.0 for s in scores]
print(processed)  # [0.92, 0.0, 0.88, 0.0, 0.95]

# Filter at the end: removes elements entirely
filtered = [s for s in scores if s > 0.5]
print(filtered)  # [0.92, 0.88, 0.95]
