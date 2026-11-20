def process_data(path):
    import json  # ❌ Import inside function: unnecessary
    with open(path) as f:
        return json.load(f)
