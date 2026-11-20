def add_item(item, cache=None):
    if cache is None:
        cache = []
    cache.append(item)
    return cache
