# predict_log.py: Simulates logging a model prediction
import sys
from datetime import datetime

# Get inputs from command line
if len(sys.argv) < 3:
    print("Usage: python3 predict_log.py <model_version> <confidence>")
    sys.exit(1)

model_version = sys.argv[1]
confidence = float(sys.argv[2])

# Create a summary string
timestamp = str(datetime.now())
summary = (
    "[" + timestamp + "] "
    "Model: " + model_version + " | "
    "Confidence: " + str(confidence) + " | "
    "Threshold: 0.5"
)

print(summary)
print("Prediction logged.")
