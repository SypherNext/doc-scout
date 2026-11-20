# write_text.py

# Write mode "w" overwrites the file
with open("output.txt", "w", encoding="utf-8") as f:
    f.write("First line\n")
    f.write("Second line\n")

# Append mode "a" adds to the end
with open("output.txt", "a", encoding="utf-8") as f:
    f.write("Third line (appended)\n")

with open("output.txt", "r", encoding="utf-8") as f:
    print(f.read())
# First line
# Second line
# Third line (appended)

os.remove("output.txt")
