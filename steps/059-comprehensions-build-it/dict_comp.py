# dict_comp.py

# Build a dict from paired lists
models = ["gpt-4", "claude-3", "llama-3"]
latencies = [1200, 1800, 900]

model_latency = {m: l for m, l in zip(models, latencies)}
print(model_latency)
# {"gpt-4": 1200, "claude-3": 1800, "llama-3": 900}

# Transform keys or values
squared = {x: x ** 2 for x in range(1, 6)}
print(squared)  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# Filter a dict
scores = {"alice": 0.95, "bob": 0.45, "carol": 0.88, "dave": 0.32}
passing = {name: score for name, score in scores.items() if score > 0.5}
print(passing)  # {"alice": 0.95, "carol": 0.88}

# Reverse a dict (swap keys and values)
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {v: k for k, v in original.items()}
print(reversed_dict)  # {1: "a", 2: "b", 3: "c"}
