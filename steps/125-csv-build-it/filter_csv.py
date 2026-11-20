import csv

rows = [
    {"model": "gpt-4", "accuracy": "0.94", "latency_ms": "1200"},
    {"model": "claude-3", "accuracy": "0.93", "latency_ms": "1800"},
    {"model": "llama-3", "accuracy": "0.89", "latency_ms": "900"},
    {"model": "gemini", "accuracy": "0.91", "latency_ms": "1500"},
]

with open("results.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["model", "accuracy", "latency_ms"])
    writer.writeheader()
    writer.writerows(rows)

# Filter: keep only models with accuracy > 0.9
filtered = []
with open("results.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        if float(row["accuracy"]) > 0.9:
            filtered.append(row)

print(f"Filtered {len(filtered)} rows")  # 3 (gpt-4, claude-3, gemini)

# Write filtered results to a new CSV
with open("high_accuracy.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.DictWriter(f, fieldnames=["model", "accuracy", "latency_ms"])
    writer.writeheader()
    writer.writerows(filtered)

# Sort by accuracy descending
sorted_rows = sorted(filtered, key=lambda r: float(r["accuracy"]), reverse=True)
for r in sorted_rows:
    print(f"{r['model']}: {r['accuracy']}")
# gpt-4: 0.94
# claude-3: 0.93
# gemini: 0.91

# Clean up
import os
os.remove("results.csv")
os.remove("high_accuracy.csv")
