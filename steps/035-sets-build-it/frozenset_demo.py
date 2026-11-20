# frozenset_demo.py

# frozenset is an immutable set: hashable, can be a dict key
frozen = frozenset(["a", "b", "c"])
# frozen.add("d")  # AttributeError: 'frozenset' object has no attribute 'add'

# Useful when you need a set in a set
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(set_of_sets)  # {frozenset({1, 2}), frozenset({3, 4})}

# Regular set cannot contain a set
# set_of_sets = { {1, 2} }  # TypeError: unhashable type: 'set'
