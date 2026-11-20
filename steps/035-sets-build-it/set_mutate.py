# set_mutate.py
items = {"a", "b", "c"}

# Add
items.add("d")
print(items)  # {'a', 'b', 'c', 'd'}

# Adding an existing element has no effect
items.add("a")
print(items)  # {'a', 'b', 'c', 'd'}: unchanged

# Remove: raises KeyError if not found
items.remove("b")
# items.remove("z")  # KeyError: 'z'

# Discard: does NOT raise an error if missing
items.discard("z")  # No error: silently does nothing

# Pop: remove and return an arbitrary element
arbitrary = items.pop()
print(arbitrary)  # Some element, e.g. 'a'

# Clear all
items.clear()
print(items)  # set()
