def add_defaults(config):
    config["temperature"] = 0.7  # Modifies the original dict!
    config["max_tokens"] = 1024
    return config

original = {"model": "gpt-4"}
result = add_defaults(original)
print(original)  # {'model': 'gpt-4', 'temperature': 0.7, 'max_tokens': 1024} (changed!)
