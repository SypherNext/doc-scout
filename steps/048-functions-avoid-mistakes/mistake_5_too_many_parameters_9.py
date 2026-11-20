from dataclasses import dataclass

@dataclass
class PipelineConfig:
    source: str
    destination: str
    format: str = "json"
    delimiter: str = ","
    encoding: str = "utf-8"
    compression: str | None = None
    max_size: int = 10_000_000
    overwrite: bool = False
    backup: bool = True
    log_level: str = "INFO"

def create_pipeline(config: PipelineConfig):
    print(f"Processing {config.source} -> {config.destination}")
