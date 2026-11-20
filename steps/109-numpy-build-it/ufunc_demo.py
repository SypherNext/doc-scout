import numpy as np

arr = np.array([0.1, 0.5, 0.9, 1.0, 2.0])

# Math ufuncs
print(np.sqrt(arr))         # [0.3162 0.7071 0.9487 1.0    1.4142]
print(np.log(arr))          # [-2.3026 -0.6931 -0.1054  0.      0.6931]
print(np.exp(arr))          # [1.1052 1.6487 2.4596 2.7183 7.3891]
print(np.square(arr))       # [0.01 0.25 0.81 1.0  4.0]

# Clip values to a range
clipped = np.clip(arr, 0.2, 0.8)
print(clipped)              # [0.2 0.5 0.8 0.8 0.8]

# Where: conditional selection
scores = np.array([0.12, 0.87, 0.45, 0.92])
passed = np.where(scores > 0.5, "pass", "fail")
print(passed)               # ['fail' 'pass' 'fail' 'pass']

# Rounding
values = np.array([1.234, 5.678, 9.012])
print(np.round(values, 1))  # [1.2 5.7 9.0]
