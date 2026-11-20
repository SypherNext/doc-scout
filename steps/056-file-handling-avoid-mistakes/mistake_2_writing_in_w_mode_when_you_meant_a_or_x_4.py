from pathlib import Path

if Path("results.csv").exists():
    append_or_merge = input("File exists. Overwrite? (y/n): ")
    mode = "w" if append_or_merge.lower() == "y" else "a"
else:
    mode = "w"
