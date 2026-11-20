# string_methods.py
raw = "  Hello, AI Engineer!  "

# Remove whitespace
print(raw.strip())        # "Hello, AI Engineer!"
print(raw.lstrip())       # "Hello, AI Engineer!  "
print(raw.rstrip())       # "  Hello, AI Engineer!"

# Split into list
csv_line = "name,role,experience"
parts = csv_line.split(",")
print(parts)              # ['name', 'role', 'experience']

# Join list into string
joined = " | ".join(parts)
print(joined)             # "name | role | experience"

# Find and replace
log = "ERROR: Model timeout"
print(log.find("Model"))  # 7: starting index of "Model"
print(log.find("GPU"))    # -1: not found
print(log.replace("ERROR", "WARNING"))  # "WARNING: Model timeout"

# Case operations
print("hello".upper())    # "HELLO"
print("WORLD".lower())    # "world"
print("hello world".title())  # "Hello World"
