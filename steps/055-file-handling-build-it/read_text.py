# read_text.py

# Create a sample file first (in a real scenario, this file already exists:
# this mirrors one entry in the sample document collection you will use later)
with open("sample.txt", "w", encoding="utf-8") as f:
    f.write("Caching Strategies\n")
    f.write("A cache stores a copy of data that is expensive to produce.\n")
    f.write("Cache-aside is the most common pattern: check cache, then source.\n")

# Read the entire file
with open("sample.txt", "r", encoding="utf-8") as f:
    content = f.read()
print(content)

# Read line by line (memory-efficient for large files)
with open("sample.txt", "r", encoding="utf-8") as f:
    for line in f:
        print(f"Read: {line.strip()}")

# Read all lines into a list
with open("sample.txt", "r", encoding="utf-8") as f:
    lines = f.readlines()
print(f"Total lines: {len(lines)}")  # 3

# Clean up
import os
os.remove("sample.txt")
