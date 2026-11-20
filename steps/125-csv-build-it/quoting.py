import csv

# Some fields contain commas or quotes, CSV handles this with quoting
rows = [
    {"model": "gpt-4", "description": "Latest OpenAI model, supports vision", "accuracy": "0.94"},
    {"model": "claude-3", "description": "Strong at reasoning & analysis", "accuracy": "0.93"},
]

with open("models.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["model", "description", "accuracy"])
    writer.writeheader()
    writer.writerows(rows)

# Read it back to see how csv module handles quoting
with open("models.csv", "r", encoding="utf-8") as f:
    content = f.read()
    print(content)
    # model,description,accuracy
    # gpt-4,"Latest OpenAI model, supports vision",0.94
    # Note: the comma inside the description is quoted

# Reading works transparently
with open("models.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['model']}: {row['description']}")

import os
os.remove("models.csv")
