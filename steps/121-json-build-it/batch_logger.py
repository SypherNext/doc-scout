import json
from pathlib import Path
from datetime import datetime

class BatchLogger:
    """Log batch inference results to JSON Lines."""

    def __init__(self, log_dir="batch_logs"):
        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(exist_ok=True)
        self.run_id = datetime.now().strftime("%Y%m%d_%H%M%S")
        self.log_path = self.log_dir / f"run_{self.run_id}.jsonl"

    def log_result(self, prompt, response, tokens_used, latency_ms):
        """Log one inference result."""
        record = {
            "timestamp": datetime.now().isoformat(),
            "prompt": prompt,
            "response": response,
            "tokens_used": tokens_used,
            "latency_ms": latency_ms,
        }
        with open(self.log_path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record) + "\n")

    def read_results(self):
        """Read all logged results."""
        results = []
        if not self.log_path.exists():
            return results
        with open(self.log_path, "r", encoding="utf-8") as f:
            for line in f:
                results.append(json.loads(line.strip()))
        return results

    def summary(self):
        """Print summary statistics."""
        results = self.read_results()
        if not results:
            print("No results logged.")
            return
        total_tokens = sum(r["tokens_used"] for r in results)
        avg_latency = sum(r["latency_ms"] for r in results) / len(results)
        print(f"Total inferences: {len(results)}")
        print(f"Total tokens: {total_tokens}")
        print(f"Average latency: {avg_latency:.0f} ms")

# Usage
logger = BatchLogger()
logger.log_result("What is Python?", "A programming language.", 6, 450)
logger.log_result("Explain JSON", "A data format.", 5, 380)
logger.log_result("What is an array?", "A collection of items.", 7, 420)

logger.summary()
# Total inferences: 3
# Total tokens: 18
# Average latency: 417 ms

# Clean up
import shutil
shutil.rmtree("batch_logs")
