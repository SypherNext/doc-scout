f = open("data.txt", "r", encoding="utf-8")
data = f.read()
# f is never closed!
