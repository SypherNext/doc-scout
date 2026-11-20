# flow_control.py

# break: exit the loop entirely
for model in ["gpt-4", "claude-3", "llama-3", "gemini-pro"]:
    if model == "llama-3":
        print(f"Found {model}, stopping search.")
        break
    print(f"Checking {model}...")
# Checking gpt-4...
# Checking claude-3...
# Found llama-3, stopping search.

# continue: skip to the next iteration
scores = [0.92, 0.45, 0.88, 0.32, 0.95]
for score in scores:
    if score < 0.5:
        continue  # Skip low-confidence predictions
    print(f"Processing score: {score}")
# Processing score: 0.92
# Processing score: 0.88
# Processing score: 0.95

# for/else: else runs only if break was NOT hit
models = ["gpt-4", "claude-3", "llama-3"]
target = "claude-4"  # Not in the list
for model in models:
    if model == target:
        print(f"Found {target}")
        break
else:
    print(f"{target} not found in the list")
