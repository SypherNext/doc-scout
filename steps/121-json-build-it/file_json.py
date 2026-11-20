import json

config = {
    "model": "claude-3-opus",
    "api_key": "sk-...",
    "parameters": {
        "temperature": 0.5,
        "max_tokens": 4096,
        "top_p": 0.9,
    },
}

# Write to file
with open("config.json", "w", encoding="utf-8") as f:
    json.dump(config, f, indent=2)

# Read from file
with open("config.json", "r", encoding="utf-8") as f:
    loaded = json.load(f)

print(loaded["model"])                   # claude-3-opus
print(loaded["parameters"]["top_p"])     # 0.9

# Clean up
import os
os.remove("config.json")
