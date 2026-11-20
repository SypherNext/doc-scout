# type_checking.py

def process_prediction(value):
    """Process a model prediction, handling different input types."""
    if value is None:
        return 0.0  # No prediction available
    if isinstance(value, bool):
        return 1.0 if value else 0.0
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        try:
            return float(value)
        except ValueError:
            return 0.0
    return 0.0

print(process_prediction(0.87))           # 0.87
print(process_prediction(None))           # 0.0
print(process_prediction(True))           # 1.0
print(process_prediction("0.95"))         # 0.95
print(process_prediction("invalid"))      # 0.0
