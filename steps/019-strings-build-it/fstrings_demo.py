# fstrings_demo.py
model = "gpt-4"
tokens = 150
latency_ms = 2342

# Old style: concatenation
log1 = "Model: " + model + " | Tokens: " + str(tokens)

# f-string: variables in {}
log2 = f"Model: {model} | Tokens: {tokens} | Latency: {latency_ms}ms"
print(log2)
# Model: gpt-4 | Tokens: 150 | Latency: 2342ms

# Expressions inside f-strings
print(f"Cost: ${tokens * 0.00015:.4f}")  # Cost: $0.0225

# Formatting: :.2f means 2 decimal places
accuracy = 0.923456
print(f"Accuracy: {accuracy:.2%}")        # Accuracy: 92.35%
print(f"Accuracy: {accuracy:.3f}")        # Accuracy: 0.923
