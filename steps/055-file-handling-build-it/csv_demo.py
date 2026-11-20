# csv_demo.py
import csv

# Write CSV
headers = ["model", "accuracy", "f1_score", "latency_ms"]
rows = [
    ["gpt-4", 0.94, 0.92, 1200],
    ["claude-3", 0.93, 0.91, 1800],
    ["llama-3", 0.89, 0.87, 900],
]

with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(headers)
    writer.writerows(rows)

# Read CSV
with open("results.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        print(row)

# Using DictReader and DictWriter
with open("results.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(f"{row['model']}: acc={row['accuracy']}")

os.remove("results.csv")
