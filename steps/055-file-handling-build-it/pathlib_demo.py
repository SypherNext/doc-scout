# pathlib_demo.py
from pathlib import Path

# Create a path object
data_dir = Path("data")
logs_dir = data_dir / "logs"  # Uses / operator for path joining

# Create directories
data_dir.mkdir(exist_ok=True)
logs_dir.mkdir(parents=True, exist_ok=True)

# Create a file in the directory
file_path = logs_dir / "experiment_1.log"
file_path.write_text("Experiment started at 2026-06-30\n", encoding="utf-8")

# Read it back
content = file_path.read_text(encoding="utf-8")
print(content)

# Check properties
print(f"Exists: {file_path.exists()}")     # True
print(f"Is file: {file_path.is_file()}")   # True
print(f"Suffix: {file_path.suffix}")       # .log
print(f"Stem: {file_path.stem}")           # experiment_1
print(f"Parent: {file_path.parent}")       # data/logs

# List all .log files in directory
for log_file in logs_dir.glob("*.log"):
    print(f"Found log: {log_file}")

# Clean up
import shutil
shutil.rmtree(data_dir)
