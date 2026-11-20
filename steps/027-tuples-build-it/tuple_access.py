# tuple_access.py
record = ("gpt-4", 2026, 0.95)

# Indexing: same as lists
print(record[0])    # gpt-4
print(record[-1])   # 0.95 (last element)

# Slicing
print(record[0:2])  # ('gpt-4', 2026)

# Iteration
for item in record:
    print(item)

# Membership
print("gpt-4" in record)  # True
