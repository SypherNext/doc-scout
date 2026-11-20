seen = set()
ordered_unique = []
for x in scores:
    if x not in seen:
        seen.add(x)
        ordered_unique.append(x)
