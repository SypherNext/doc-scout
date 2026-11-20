# unpacking.py

# Basic unpacking
model, year, score = ("gpt-4", 2026, 0.95)
print(model)   # gpt-4
print(year)    # 2026
print(score)   # 0.95

# Unpacking works with any iterable, including lists and the tuple returned by functions
coordinates = (10, 20)
x, y = coordinates
print(x, y)  # 10 20

# Swapping variables: uses tuple packing and unpacking
a, b = 5, 10
a, b = b, a
print(a, b)  # 10 5

# Ignoring values with _
_, middle, _ = (1, 2, 3)
print(middle)  # 2

# Extended unpacking with * (Python 3+)
first, *rest = (1, 2, 3, 4)
print(first)  # 1
print(rest)   # [2, 3, 4] (note: rest is a list)
