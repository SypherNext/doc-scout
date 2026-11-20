import numpy as np

arr = np.array([10, 20, 30, 40, 50, 60])

# Regular indexing works like lists
print(arr[0])       # 10
print(arr[-1])      # 60

# Slice: start:stop:step
print(arr[1:4])     # [20 30 40]
print(arr[::2])     # [10 30 50]

# 2D indexing
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(matrix[0, 1])    # 2: row 0, column 1
print(matrix[1])       # [4 5 6]: entire row 1
print(matrix[:, 1])    # [2 5 8]: entire column 1

# Boolean indexing: filter with a condition
scores = np.array([0.12, 0.87, 0.45, 0.92, 0.33, 0.78])
high = scores[scores > 0.5]
print(high)        # [0.87 0.92 0.78]

# Combine conditions with & and |
in_range = scores[(scores > 0.3) & (scores < 0.8)]
print(in_range)    # [0.45 0.33 0.78]

# Fancy indexing: select by index array
indices = np.array([0, 2, 4])
print(scores[indices])  # [0.12 0.45 0.33]

view = arr[1:4]
view[0] = 999
print(arr)  # [10 999 30 40 50 60]: original was modified!
