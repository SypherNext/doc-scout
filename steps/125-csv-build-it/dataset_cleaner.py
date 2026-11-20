import csv
from pathlib import Path
import re

def clean_csv(input_path, output_path, expected_columns=None):
    """Read a CSV, clean it, and write the cleaned version."""

    def is_valid_row(row):
        """Check if a row is valid."""
        if expected_columns and len(row) != expected_columns:
            return False
        # All values should be non-empty strings
        return all(cell.strip() for cell in row)

    with open(input_path, "r", newline="", encoding="utf-8") as fin:
        reader = csv.reader(fin)
        header = next(reader)  # Always consume the header row first

        valid_rows = []
        skipped = 0

        for row in reader:
            if is_valid_row(row):
                # Strip whitespace from each cell
                cleaned = [cell.strip() for cell in row]
                valid_rows.append(cleaned)
            else:
                skipped += 1

    with open(output_path, "w", newline="", encoding="utf-8") as fout:
        writer = csv.writer(fout)
        if header:
            writer.writerow(header)
        writer.writerows(valid_rows)

    return len(valid_rows), skipped

# Create a dirty CSV to clean
with open("dirty.csv", "w", newline="", encoding="utf-8") as f:
    f.write("name,score,label\n")
    f.write("Alice,0.95,positive\n")
    f.write("Bob,,positive\n")         # missing score
    f.write("Carol,0.88,negative\n")
    f.write("Dave,0.72,\n")             # empty label
    f.write(" Eve , 0.91 , positive\n") # extra whitespace
    f.write("Frank,0.85,positive,extra\n")  # too many columns

valid, skipped = clean_csv("dirty.csv", "clean.csv", expected_columns=3)
print(f"Valid rows: {valid}, Skipped: {skipped}")
# Valid rows: 3 (Alice, Carol, Eve), Skipped: 3 (Bob, Dave, Frank)

# Show cleaned file
with open("clean.csv", "r", encoding="utf-8") as f:
    print(f.read())
# name,score,label
# Alice,0.95,positive
# Carol,0.88,negative
# Eve,0.91,positive

# Clean up
import os
os.remove("dirty.csv")
os.remove("clean.csv")
