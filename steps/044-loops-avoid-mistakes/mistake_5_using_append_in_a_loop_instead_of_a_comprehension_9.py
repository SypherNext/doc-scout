# Filter + transform
results = [process(x) for x in data if x > 0]

# Dict comprehension
square_map = {x: x ** 2 for x in range(10)}

# Set comprehension
unique_lengths = {len(word) for word in words}
