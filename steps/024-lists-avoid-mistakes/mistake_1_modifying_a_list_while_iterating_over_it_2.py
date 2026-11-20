numbers = [1, 2, 3, 4, 5]
for n in numbers.copy():
    if n % 2 == 0:
        numbers.remove(n)
