import numpy as np

arr = np.array([1, 2, 3, 4, 5])
mask = arr > 2
subset = arr[mask]  # This IS a copy
subset[0] = 999
print(arr)          # [1 2 3 4 5]: original unchanged
