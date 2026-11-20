# Inefficient and verbose
squares = []
for x in range(100):
    squares.append(x ** 2)

# Better
squares = [x ** 2 for x in range(100)]
