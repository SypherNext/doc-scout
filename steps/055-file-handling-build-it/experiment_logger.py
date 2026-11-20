# experiment_logger.py: Log experiment results to files

import json
from pathlib import Path
from datetime import datetime

class ExperimentLogger:
    """Logs experiment results to structured files."""

    def __init__(self, experiment_dir="experiments"):
        self.base_dir = Path(experiment_dir)
        self.base_dir.mkdir(exist_ok=True)

    def log_run(self, model_name, config, metrics):
        """Log a single experiment run."""
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        run_name = f"{model_name}_{timestamp}"

        # Create a directory for this run
        run_dir = self.base_dir / run_name
        run_dir.mkdir(parents=True)

        # Save config
        config_path = run_dir / "config.json"
        config_path.write_text(json.dumps(config, indent=2), encoding="utf-8")

        # Save metrics
        metrics_path = run_dir / "metrics.json"
        metrics_path.write_text(json.dumps(metrics, indent=2), encoding="utf-8")

        # Summary line
        summary_path = self.base_dir / "summary.csv"
        header = "run_name,model,accuracy,f1_score\n"
        line = f"{run_name},{model_name},{metrics.get('accuracy', 'N/A')},{metrics.get('f1', 'N/A')}\n"

        if not summary_path.exists():
            summary_path.write_text(header, encoding="utf-8")

        with open(summary_path, "a", encoding="utf-8") as f:
            f.write(line)

        print(f"Logged run: {run_name}")
        return run_name

# Usage
logger = ExperimentLogger()
logger.log_run(
    "gpt-4",
    config={"temperature": 0.7, "max_tokens": 2048},
    metrics={"accuracy": 0.94, "f1": 0.92, "latency_ms": 1200},
)
logger.log_run(
    "claude-3",
    config={"temperature": 0.5, "max_tokens": 4096},
    metrics={"accuracy": 0.93, "f1": 0.91, "latency_ms": 1800},
)

# Read back the summary
summary_path = Path("experiments/summary.csv")
if summary_path.exists():
    print(summary_path.read_text(encoding="utf-8"))

# Clean up
import shutil
shutil.rmtree("experiments")
