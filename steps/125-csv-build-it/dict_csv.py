import csv

data = [
    {"model": "gpt-4", "accuracy": 0.94, "latency_ms": 1200},
    {"model": "claude-3", "accuracy": 0.93, "latency_ms": 1800},
    {"model": "llama-3", "accuracy": 0.89, "latency_ms": 900},
]

# Write with DictWriter
with open("models.csv", "w", newline="", encoding="utf-8") as f:
    fieldnames = ["model", "accuracy", "latency_ms"]
    writer = csv.DictWriter(f, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerows(data)

# Read with DictReader, access by column name
with open("models.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        acc = float(row["accuracy"])
        lat = int(row["latency_ms"])
        print(f"{row['model']}: acc={acc:.2f}, lat={lat}ms")

# Clean up
import os
os.remove("models.csv")
