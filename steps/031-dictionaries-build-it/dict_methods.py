# dict_methods.py
record = {"name": "Alice", "role": "engineer", "years": 5}

# Get all keys: view object (iterable, not a list)
print(record.keys())     # dict_keys(['name', 'role', 'years'])

# Get all values
print(record.values())   # dict_values(['Alice', 'engineer', 5])

# Get all key-value pairs as tuples
print(record.items())    # dict_items([('name', 'Alice'), ('role', 'engineer'), ('years', 5)])

# Convert to list if needed
keys = list(record.keys())

# Check if a key exists
print("name" in record)      # True
print("salary" in record)    # False

# Merge another dictionary
updates = {"role": "senior engineer", "salary": 120000}
record.update(updates)
print(record)
# {'name': 'Alice', 'role': 'senior engineer', 'years': 5, 'salary': 120000}
