import csv

# Some exports use tab, semicolon, or pipe
data = "model|accuracy|latency_ms\ngpt-4|0.94|1200\n"

# Wrong, comma is the default delimiter
reader = csv.reader(data.splitlines())
for row in reader:
    print(row)  # ['model|accuracy|latency_ms'], entire row as one field!

# Correct, specify the delimiter
reader = csv.reader(data.splitlines(), delimiter="|")
for row in reader:
    print(row)  # ['model', 'accuracy', 'latency_ms']
