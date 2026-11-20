# Slow: O(n²) due to repeated copying
result = ""
for i in range(1000):
    result += str(i) + ","

# Fast: O(n)
parts = []
for i in range(1000):
    parts.append(str(i))
result = ",".join(parts)
