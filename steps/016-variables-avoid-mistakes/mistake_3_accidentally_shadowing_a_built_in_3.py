list = [1, 2, 3]        # Shadows the built-in list()
print(list([4, 5, 6]))  # TypeError: 'list' object is not callable
