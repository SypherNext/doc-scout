a = [1, 2]
a.append([3, 4])
print(a)  # [1, 2, [3, 4]]: nested list added as one element

b = [1, 2]
b.extend([3, 4])
print(b)  # [1, 2, 3, 4]: elements added individually
