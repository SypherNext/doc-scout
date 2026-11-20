import numpy as np

a = np.array([1, 2, 3])       # shape (3,)
b = np.array([[1, 2], [3, 4], [5, 6]])  # shape (3, 2)

try:
    result = a + b  # ValueError: operands could not be broadcast together
except ValueError as e:
    print(e)  # shapes (3,) and (3,2) not aligned


a_2d = a[:, np.newaxis]  # shape (3, 1): now broadcastable with (3, 2)
print(a_2d + b)
# [[ 2  3]
#  [ 5  6]
#  [ 8  9]]
