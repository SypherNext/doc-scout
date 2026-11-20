def add_item(item, cache=[]):  # ❌ Dangerous default
    cache.append(item)
    return cache

print(add_item("a"))  # ['a']
print(add_item("b"))  # ['a', 'b']: Not what you expect!
