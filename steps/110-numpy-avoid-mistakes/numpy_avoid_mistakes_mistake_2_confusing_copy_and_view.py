import numpy as np

arr = np.array([1, 2, 3, 4, 5])
subset = arr[:3]    # View, not a copy
subset[0] = 999
print(arr)          # [999   2   3   4   5]: original changed!

# Correct: explicit copy
subset = arr[:3].copy()
subset[0] = 0
print(arr)          # [999   2   3   4   5]: original unchanged
