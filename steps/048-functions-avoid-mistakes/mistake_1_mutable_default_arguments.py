def add_item(item, cache=[]):  # ❌
    cache.append(item)
    return cache

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b'] (the same list!)
print(add_item("c"))  # ['a', 'b', 'c'] (unintended accumulation)
