# set_comp.py

# Unique squared values: duplicates collapse
numbers = [1, 2, 2, 3, 3, 3, 4]
unique_squares = {n ** 2 for n in numbers}
print(unique_squares)  # {16, 1, 4, 9}: order not guaranteed

# Collect unique first letters
words = ["apple", "banana", "avocado", "blueberry", "cherry"]
first_letters = {w[0] for w in words}
print(first_letters)  # {"a", "b", "c"}

# Filtered set comprehension
long_words = {w for w in words if len(w) > 6}
print(long_words)  # {"blueberry", "avocado"}
