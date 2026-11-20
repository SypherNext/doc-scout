import csv

with open("data.csv", "w", newline="", encoding="utf-8") as f:
    f.write("value\n0.94\n0.93\n")

with open("data.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    next(reader)  # skip header
    for row in reader:
        total = row[0] + 0.05  # TypeError: can only concatenate str (not "float") to str


value = float(row[0])  # Convert to float
