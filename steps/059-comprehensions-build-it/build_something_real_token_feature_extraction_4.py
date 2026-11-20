# Build a matrix of feature vectors: one row per text
import json

for i, text in enumerate(texts):
    row = {k: v[i] for k, v in features.items()}
    print(f"Text {i + 1}: {json.dumps(row)}")
