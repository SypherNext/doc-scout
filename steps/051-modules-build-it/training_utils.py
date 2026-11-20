# training_utils.py

def load_dataset(path):
    print(f"Loading dataset from {path}...")
    return ["sample1", "sample2", "sample3"]

# Without guard: this runs on import!
# print("Module loaded!")  # ❌ Runs when imported

# With guard: only runs when executed directly
if __name__ == "__main__":
    print("Testing load_dataset...")
    data = load_dataset("test.csv")
    print(f"Loaded {len(data)} samples.")
