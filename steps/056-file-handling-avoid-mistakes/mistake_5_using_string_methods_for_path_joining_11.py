from pathlib import Path

config_dir = Path.home() / ".config" / "myapp"
config_dir.mkdir(parents=True, exist_ok=True)
config_path = config_dir / "settings.json"
