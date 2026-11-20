import csv

# TSV, tab-separated values
tsv_data = "model\taccuracy\tlatency_ms\ngpt-4\t0.94\t1200\nclaude-3\t0.93\t1800\n"

with open("models.tsv", "w", newline="", encoding="utf-8") as f:
    f.write(tsv_data)

# Read TSV with delimiter="\t"
with open("models.tsv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f, delimiter="\t")
    for row in reader:
        print(f"{row['model']}: {row['accuracy']}")

# Custom delimiter, semicolons (common in European CSV)
csv_data = "model;accuracy;latency_ms\ngpt-4;0.94;1200\n"
reader = csv.DictReader(csv_data.splitlines(), delimiter=";")
for row in reader:
    print(f"{row['model']}: {row['accuracy']}")

import os
os.remove("models.tsv")
