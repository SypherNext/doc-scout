import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

# Element-wise arithmetic: no loop needed
print(a + b)      # [11 22 33 44]
print(a * b)      # [10 40 90 160]
print(b - a)      # [ 9 18 27 36]
print(b / a)      # [10. 10. 10. 10.]
print(a ** 2)     # [ 1  4  9 16]

# Comparisons produce boolean arrays
print(a > 2)      # [False False  True  True]

# Aggregate functions
print(a.sum())       # 10
print(a.mean())      # 2.5
print(a.max())       # 4
print(a.min())       # 1
print(a.std())       # 1.1180...: standard deviation
print(a.var())       # 1.25: variance

# Axis argument for 2D: 0 = column-wise, 1 = row-wise
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix.sum(axis=0))  # [5 7 9]: sum each column
print(matrix.sum(axis=1))  # [6 15]: sum each row
