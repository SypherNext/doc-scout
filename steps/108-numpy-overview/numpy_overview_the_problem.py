scores = [0.12, 0.87, 0.45, 0.92, 0.33, 0.78]
threshold = 0.5

result = []
for s in scores:
    if s > threshold:
        result.append(s ** 2)

mean = sum(result) / len(result)  # (0.7569 + 0.8464 + 0.6084) / 3 = 0.7372...
