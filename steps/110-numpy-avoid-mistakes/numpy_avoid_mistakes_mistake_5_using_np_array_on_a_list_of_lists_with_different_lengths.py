import numpy as np

# Jagged list: inner lists have different lengths
jagged = [[1, 2, 3], [4, 5]]

try:
    arr = np.array(jagged)  # Creates array of Python lists, not 2D!
except ValueError as e:
    print(e)

# What you actually get:
arr = np.array(jagged, dtype=object)
print(arr)          # [list([1, 2, 3]) list([4, 5])]
print(arr.shape)    # (2,): not (2, 3)!
