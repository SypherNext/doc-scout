import numpy as np

arr = np.arange(12)  # [0 1 2 3 4 5 6 7 8 9 10 11]

# Reshape to 3 rows, 4 columns
reshaped = arr.reshape(3, 4)
print(reshaped)
# [[ 0  1  2  3]
#  [ 4  5  6  7]
#  [ 8  9 10 11]]

# Flatten back to 1D
flat = reshaped.flatten()
print(flat)  # [0 1 2 3 4 5 6 7 8 9 10 11]

# Transpose: swap rows and columns
transposed = reshaped.T
print(transposed.shape)  # (4, 3)
# [[ 0  4  8]
#  [ 1  5  9]
#  [ 2  6 10]
#  [ 3  7 11]]

# Reshape with -1 (automatically infer dimension)
auto = arr.reshape(2, -1)   # 2 rows, infer columns
print(auto.shape)            # (2, 6)
