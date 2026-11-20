import json

# For a 2 GB JSON file: this will crash or swap heavily
with open("huge_dataset.json", "r", encoding="utf-8") as f:
    data = json.load(f)  # 2 GB in memory!
