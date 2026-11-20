# Fragile: breaks on Windows with backslashes
path = data_dir + "/" + filename

# Better: works cross-platform
from pathlib import Path
path = Path(data_dir) / filename
