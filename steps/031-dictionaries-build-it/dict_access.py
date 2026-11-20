# dict_access.py
config = {"model": "gpt-4", "temperature": 0.7, "max_tokens": 2048}

# Access by key
print(config["model"])  # gpt-4

# Using get(): returns None (or a default) if key is missing
print(config.get("model"))       # gpt-4
print(config.get("top_p"))       # None: key does not exist
print(config.get("top_p", 1.0))  # 1.0: default value returned

# KeyError with bracket access
# print(config["top_p"])  # KeyError: 'top_p'

# Add or update
config["temperature"] = 0.5   # Update existing key
config["top_p"] = 0.9         # Add new key
print(config)
# {'model': 'gpt-4', 'temperature': 0.5, 'max_tokens': 2048, 'top_p': 0.9}

# Delete a key
del config["top_p"]
print(config)
# {'model': 'gpt-4', 'temperature': 0.5, 'max_tokens': 2048}

# Pop: remove and return the value
value = config.pop("temperature")
print(value)    # 0.5
print(config)   # {'model': 'gpt-4', 'max_tokens': 2048}
