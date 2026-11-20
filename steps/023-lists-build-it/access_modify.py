# access_modify.py
items = ["a", "b", "c", "d", "e"]

# Access by index
print(items[0])    # a
print(items[-1])   # e: last element
print(items[1:3])  # ['b', 'c']: slice (stop is exclusive)

# Modify by index: lists are mutable
items[0] = "z"
print(items)       # ['z', 'b', 'c', 'd', 'e']

# Slice assignment: replace a range
items[1:3] = ["x", "y"]
print(items)       # ['z', 'x', 'y', 'd', 'e']

# Delete by index
del items[0]
print(items)       # ['x', 'y', 'd', 'e']
