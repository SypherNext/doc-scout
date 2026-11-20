result = []
for row in matrix:
    for col in row:
        for z in col:
            if z > 0:
                result.append(z)
