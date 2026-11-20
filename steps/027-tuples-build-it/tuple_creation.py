# tuple_creation.py

# Parentheses are optional: the comma creates the tuple
empty = ()
single = (42,)          # Note the trailing comma, without it, it is just an int
pair = (1, 2)           # Two elements
triple = 1, 2, 3        # Parentheses optional
nested = (1, (2, 3))    # Nested tuples
mixed = (42, "hello", True, 3.14)

# From an iterable
chars = tuple("abc")
print(chars)  # ('a', 'b', 'c')

# From a list
converted = tuple([1, 2, 3])
print(converted)  # (1, 2, 3)
