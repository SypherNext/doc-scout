import numpy as np

# From a list
arr = np.array([1, 2, 3, 4, 5])
print(arr)          # [1 2 3 4 5]
print(arr.dtype)    # int64 (or int32 on some platforms)
print(arr.shape)    # (5,)

# 2D array from nested lists
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.shape)  # (2, 3)
print(matrix)
# [[1 2 3]
#  [4 5 6]]

# Built-in creation functions
zeros = np.zeros((3, 4))     # 3x4 matrix of zeros
ones = np.ones((2, 3))       # 2x3 matrix of ones
identity = np.eye(4)         # 4x4 identity matrix
print(identity)
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

# Evenly spaced values
seq = np.arange(0, 10, 2)    # start=0, stop=10, step=2 → [0, 2, 4, 6, 8]
lin = np.linspace(0, 1, 5)   # 5 values from 0 to 1 inclusive → [0., 0.25, 0.5, 0.75, 1.]

# Random arrays
rng = np.random.default_rng(seed=42)
rand_vals = rng.random(4)        # 4 random floats in [0, 1)
rand_norm = rng.normal(0, 1, 3)  # 3 samples from N(0, 1)
print(f"{rand_vals}")

arr32 = np.array([1, 2, 3], dtype=np.float32)
arr64 = np.array([1, 2, 3], dtype=np.float64)
print(arr32.dtype)  # float32
print(arr64.dtype)  # float64
