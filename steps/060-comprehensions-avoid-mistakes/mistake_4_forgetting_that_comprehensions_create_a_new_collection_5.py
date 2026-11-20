# List comprehension: builds entire list in memory
big = [x * 2 for x in range(10_000_000)]  # ~80 MB

# Generator expression: produces values on demand
big = (x * 2 for x in range(10_000_000))   # ~0 MB
