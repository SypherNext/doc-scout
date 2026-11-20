import csv

# Excel on Windows often saves CSV with a UTF-8 BOM (\\ufeff)
# This makes the first field of the first row include the BOM
data = "﻿model,accuracy\ngpt-4,0.94\n"

reader = csv.DictReader(data.splitlines())
for row in reader:
    print(list(row.keys()))
    # ['\\ufeffmodel', 'accuracy'], note the BOM prefix!


with open("data.csv", "r", newline="", encoding="utf-8-sig") as f:
    reader = csv.DictReader(f)
    for row in reader:
        print(row)  # BOM is stripped by utf-8-sig encoding
