# JSON Lines format: each line is a complete JSON object
with open("data.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        record = json.loads(line)
        process(record)
