# Pre-3.7: order was NOT guaranteed
# 3.7+: insertion order IS preserved
config = {"z": 1, "a": 2, "m": 3}
print(list(config.keys()))  # ['z', 'a', 'm']: insertion order
