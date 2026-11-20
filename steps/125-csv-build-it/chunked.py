import csv

# Generate a larger sample (10,000 rows); in a real scenario this would be a file on disk
import io
buf = io.StringIO()
writer = csv.writer(buf)
writer.writerow(["id", "value", "category"])
for i in range(10000):
    writer.writerow([i, float(i % 100), "A" if i % 2 == 0 else "B"])
buf.seek(0)

# Process in chunks of 1000
chunk_size = 1000
reader = csv.DictReader(buf)
chunk = []
for i, row in enumerate(reader):
    row["value"] = float(row["value"])
    chunk.append(row)
    if (i + 1) % chunk_size == 0:
        # Process chunk (e.g., compute partial stats)
        print(f"Processed rows 0-{i}: sum = {sum(r['value'] for r in chunk):.0f}")
        chunk = []

# Process remaining rows
if chunk:
    print(f"Final partial chunk: {len(chunk)} rows")
