import numpy as np

arr = np.array([1, 2, 3, 4, 5])

# Slow: Python loop
result = []
for x in arr:
    result.append(x ** 2)

# Fast: vectorized
result = arr ** 2
