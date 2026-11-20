# Produces a list of tuples, not a dict
result = [(x, x ** 2) for x in range(5)]
# [(0, 0), (1, 1), (2, 4), (3, 9), (4, 16)]

# What you probably wanted:
result = {x: x ** 2 for x in range(5)}
# {0: 0, 1: 1, 2: 4, 3: 9, 4: 16}
