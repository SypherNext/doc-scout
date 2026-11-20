# Bug: skips elements
items = [1, 2, 3, 4, 5]
for item in items:
    if item % 2 == 0:
        items.remove(item)
print(items)  # [1, 3, 5]: works here but not reliable
