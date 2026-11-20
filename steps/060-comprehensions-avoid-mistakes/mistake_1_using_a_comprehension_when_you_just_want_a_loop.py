# Side effect: confusing
[print(x) for x in data]  # Creates a list of None values!

# Better
for x in data:
    print(x)
