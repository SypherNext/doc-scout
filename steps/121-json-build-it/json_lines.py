import json

# Write JSON Lines
records = [
    {"id": 1, "prompt": "Hello", "response": "Hi there!"},
    {"id": 2, "prompt": "How are you?", "response": "I am good."},
    {"id": 3, "prompt": "What is AI?", "response": "Artificial intelligence."},
]

with open("data.jsonl", "w", encoding="utf-8") as f:
    for record in records:
        f.write(json.dumps(record) + "\n")

# Read JSON Lines: memory-efficient for large files
with open("data.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        record = json.loads(line.strip())
        print(f"ID {record['id']}: {record['prompt']}")

# Clean up
import os
os.remove("data.jsonl")
