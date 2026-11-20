# list_comp.py
numbers = [1, 2, 3, 4, 5]

# Map: transform every element
doubled = [n * 2 for n in numbers]
print(doubled)  # [2, 4, 6, 8, 10]

# Filter: keep only elements matching a condition
evens = [n for n in numbers if n % 2 == 0]
print(evens)  # [2, 4]

# Map + filter: transform kept elements
high_doubled = [n * 2 for n in numbers if n > 3]
print(high_doubled)  # [8, 10]

# With a string method
texts = ["  hello  ", "WORLD", "  Python  "]
cleaned = [t.strip().lower() for t in texts]
print(cleaned)  # ["hello", "world", "python"]
