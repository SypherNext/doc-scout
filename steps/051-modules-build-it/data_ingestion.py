# data_ingestion.py
"""Module for loading data from multiple sources."""

import json
import csv

def load_json(path):
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def load_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        return list(csv.DictReader(f))

if __name__ == "__main__":
    # Test loading
    import tempfile, os
    with tempfile.NamedTemporaryFile(mode="w", suffix=".csv", delete=False) as f:
        f.write("name,score\nAlice,0.95\nBob,0.87")
        tmp_path = f.name
    data = load_csv(tmp_path)
    print(f"Loaded {len(data)} records from CSV")
    os.unlink(tmp_path)
