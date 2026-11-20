# On Windows, this may fail with UnicodeDecodeError
with open("data.txt", "r") as f:  # Uses system default encoding!
    data = f.read()
