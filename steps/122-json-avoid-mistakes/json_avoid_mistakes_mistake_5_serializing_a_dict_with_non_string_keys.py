import json

data = {1: "one", 2: "two"}

# Works: keys are converted to strings
json_str = json.dumps(data)
print(json_str)  # {"1": "one", "2": "two"}

# But the round-trip changes the type!
parsed = json.loads(json_str)
print(list(parsed.keys()))  # ['1', '2']: strings, not ints!


data = {1: "one", 2: "two"}
# Convert keys explicitly to preserve type info
serializable = {str(k): {"key_type": type(k).__name__, "value": v}
                for k, v in data.items()}
