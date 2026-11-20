config = {"model": "gpt-4", "temperature": 0.7, "max_tokens": 2048}
for key in config:
    if key.startswith("max_"):
        del config[key]  # RuntimeError: dictionary changed size during iteration
