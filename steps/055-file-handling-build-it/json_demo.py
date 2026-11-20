# json_demo.py
import json

# Python dict -> JSON string
data = {
    "model": "gpt-4",
    "parameters": {
        "temperature": 0.7,
        "max_tokens": 2048,
    },
    "tags": ["production", "v2"],
}

# Write JSON to file
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2)

# Read JSON from file
with open("config.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["model"])               # gpt-4
print(loaded["parameters"]["temperature"])  # 0.7

# JSON string in memory
json_str = json.dumps(data, indent=2)
print(json_str)

# Parse JSON string
parsed = json.loads(json_str)
print(parsed["tags"])  # ['production', 'v2']

os.remove("config.json")
