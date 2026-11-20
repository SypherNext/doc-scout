# dict_creation.py

# Empty dict
empty = {}
also_empty = dict()

# String keys: most common
config = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 2048,
}

# Integer keys: useful for sparse arrays
number_map = {0: "zero", 1: "one", 2: "two"}

# Mixed types: possible but avoid for readability
mixed = {"key": 42, 100: "hundred", (1, 2): "tuple key"}

# From paired sequences using zip
keys = ["name", "role", "years"]
values = ["Alice", "engineer", 5]
person = dict(zip(keys, values))
print(person)  # {'name': 'Alice', 'role': 'engineer', 'years': 5}
