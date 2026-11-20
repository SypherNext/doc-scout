# zip_demo.py
models = ["gpt-4", "claude-3", "llama-3"]
latencies_ms = [1200, 1800, 900]
costs_per_1k = [0.03, 0.015, 0.002]

for model, latency, cost in zip(models, latencies_ms, costs_per_1k):
    print(f"{model}: {latency}ms, ${cost}/1k tokens")

# gpt-4: 1200ms, $0.03/1k tokens
# claude-3: 1800ms, $0.015/1k tokens
# llama-3: 900ms, $0.002/1k tokens

# zip stops at the shortest sequence
short = [1, 2, 3]
longer = ["a", "b", "c", "d"]
for a, b in zip(short, longer):
    print(a, b)
# 1 a
# 2 b
# 3 c : "d" is not included
