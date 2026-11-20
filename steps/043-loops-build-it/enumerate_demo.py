# enumerate_demo.py
configs = [
    {"model": "gpt-4", "temperature": 0.7},
    {"model": "claude-3", "temperature": 0.5},
    {"model": "llama-3", "temperature": 0.3},
]

for index, config in enumerate(configs):
    print(f"{index}: {config['model']} at temp {config['temperature']}")

# 0: gpt-4 at temp 0.7
# 1: claude-3 at temp 0.5
# 2: llama-3 at temp 0.3

# Start from a non-zero index
for index, item in enumerate(["a", "b", "c"], start=1):
    print(f"{index}: {item}")
# 1: a
# 2: b
# 3: c
