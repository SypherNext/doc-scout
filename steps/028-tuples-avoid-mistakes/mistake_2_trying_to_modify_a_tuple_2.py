t = (1, 2, 3)
t[0] = 99  # TypeError: 'tuple' object does not support item assignment
t.append(4)  # AttributeError: 'tuple' object has no attribute 'append'
