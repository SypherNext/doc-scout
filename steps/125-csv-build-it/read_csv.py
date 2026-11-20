import csv

# Create a sample CSV
with open("models.csv", "w", newline="", encoding="utf-8") as f:
    f.write("model,accuracy,latency_ms\n")
    f.write("gpt-4,0.94,1200\n")
    f.write("claude-3,0.93,1800\n")
    f.write("llama-3,0.89,900\n")

# Read with csv.reader, each row is a list of strings
with open("models.csv", "r", newline="", encoding="utf-8") as f:
    reader = csv.reader(f)
    header = next(reader)  # Read the first row as header
    print(f"Header: {header}")  # ['model', 'accuracy', 'latency_ms']
    for row in reader:
        print(f"Model: {row[0]}, Accuracy: {row[1]}, Latency: {row[2]}")

# Clean up
import os
os.remove("models.csv")
