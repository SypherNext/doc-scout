import csv

# Wrong, causes blank lines on Windows when writing
with open("data.csv", "w", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["a", "b"])

# Correct
with open("data.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
