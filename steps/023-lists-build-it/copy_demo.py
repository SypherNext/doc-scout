# copy_demo.py

# Assignment creates a reference, NOT a copy
original = [1, 2, 3]
alias = original
alias.append(4)
print(original)  # [1, 2, 3, 4]: original changed too!

# Shallow copy with .copy() or list() or [:]
copy1 = original.copy()
copy2 = list(original)
copy3 = original[:]

copy1.append(5)
print(original)  # [1, 2, 3, 4]: unchanged
print(copy1)     # [1, 2, 3, 4, 5]

# Deep copy needed for nested lists
nested = [[1, 2], [3, 4]]
shallow = nested.copy()
shallow[0].append(99)
print(nested)    # [[1, 2, 99], [3, 4]]: inner list shared!

import copy
deep = copy.deepcopy(nested)
deep[0].append(100)
print(nested)    # [[1, 2, 99], [3, 4]]: unchanged
