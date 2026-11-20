import numpy as np

# Scalar + array: scalar is broadcast to match array
arr = np.array([1, 2, 3, 4])
print(arr + 10)   # [11 12 13 14]
print(arr * 2)    # [ 2  4  6  8]

# 1D + 2D: row is broadcast across all rows
matrix = np.ones((3, 4))          # 3x4 matrix
row = np.array([10, 20, 30, 40])  # 1D, length 4

result = matrix + row
print(result)
# [[11. 21. 31. 41.]
#  [11. 21. 31. 41.]
#  [11. 21. 31. 41.]]

# Column vector broadcast across all columns
col = np.array([[1], [2], [3]])   # shape (3, 1)
result2 = matrix + col
print(result2)
# [[2. 2. 2. 2.]
#  [3. 3. 3. 3.]
#  [4. 4. 4. 4.]]
