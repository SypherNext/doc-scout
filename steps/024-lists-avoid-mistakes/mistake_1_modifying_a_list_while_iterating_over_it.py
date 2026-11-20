# Bug: removes only every other element
numbers = [1, 2, 3, 4, 5]
for n in numbers:
    if n % 2 == 0:
        numbers.remove(n)
print(numbers)  # [1, 3, 5]: works here by luck, fails in general
