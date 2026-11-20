items = {1, 2, 3, 4, 5}
for item in items:
    if item % 2 == 0:
        items.remove(item)  # RuntimeError: set changed size during iteration
