# indexing_slicing.py
text = "AIDeveloper"

# Indexing: get one character
print(text[0])   # A
print(text[2])   # D
print(text[-1])  # r: last character
print(text[-2])  # e: second-to-last

# Slicing (get a substring): text[start:stop:step]
# stop is exclusive (does not include stop index)
print(text[0:2])   # AI
print(text[2:])    # Developer: from index 2 to end
print(text[:2])    # AI: from start to index 2 (exclusive)
print(text[::2])   # ADeoe: every second character
print(text[::-1])  # repoleveDIA: reverse the string
