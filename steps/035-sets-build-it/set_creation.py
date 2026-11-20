# set_creation.py

# Empty set: must use set(), not {}
empty_set = set()
not_a_set = {}  # This is an empty dict, not a set!

# Set with values
animals = {"cat", "dog", "emu", "fox"}

# From a list (deduplicates automatically)
numbers = set([1, 2, 2, 3, 3, 3])
print(numbers)  # {1, 2, 3}

# From a string (gives unique characters)
chars = set("hello")
print(chars)    # {'h', 'e', 'l', 'o'}: order may vary
