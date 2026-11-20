import json
from datetime import datetime
import numpy as np

# Python types that json.dumps cannot handle by default
data = {
    "event": "training_start",
    "timestamp": datetime.now(),
    "learning_rate": 0.001,
    "scores": np.array([0.92, 0.88, 0.95]),
}

def custom_serializer(obj):
    """Convert non-serializable types to JSON-safe types."""
    if isinstance(obj, datetime):
        return obj.isoformat()
    if isinstance(obj, np.ndarray):
        return obj.tolist()
    raise TypeError(f"Object of type {type(obj)} is not JSON serializable")

json_str = json.dumps(data, default=custom_serializer, indent=2)
print(json_str)
# {
#   "event": "training_start",
#   "timestamp": "2026-06-30T12:00:00",
#   "learning_rate": 0.001,
#   "scores": [0.92, 0.88, 0.95]
# }
