# dict_iteration.py
config = {"model": "gpt-4", "temperature": 0.7, "max_tokens": 2048}

# Iterate over keys (default)
for key in config:
    print(key)  # model, temperature, max_tokens

# Iterate over key-value pairs (preferred)
for key, value in config.items():
    print(f"{key}: {value}")

# Iterate over values
for value in config.values():
    print(value)
