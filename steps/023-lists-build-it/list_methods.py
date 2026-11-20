# list_methods.py
numbers = []

# Add to the end
numbers.append(10)
numbers.append(20)
numbers.append(30)
print(numbers)  # [10, 20, 30]

# Insert at a position
numbers.insert(1, 15)
print(numbers)  # [10, 15, 20, 30]

# Extend with another list
numbers.extend([40, 50])
print(numbers)  # [10, 15, 20, 30, 40, 50]

# Remove by value (first occurrence)
numbers.remove(20)
print(numbers)  # [10, 15, 30, 40, 50]

# Pop by index (default last)
last = numbers.pop()
print(last)      # 50
print(numbers)   # [10, 15, 30, 40]

first = numbers.pop(0)
print(first)     # 10
print(numbers)   # [15, 30, 40]

# Find index of a value
print(numbers.index(30))  # 1

# Check membership
print(30 in numbers)   # True
print(99 in numbers)   # False

# Count occurrences
nums = [1, 2, 2, 3, 2]
print(nums.count(2))   # 3

# Sort in-place
numbers.sort()
print(numbers)  # [15, 30, 40]

# Reverse in-place
numbers.reverse()
print(numbers)  # [40, 30, 15]
