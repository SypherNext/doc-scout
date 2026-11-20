# range_demo.py

# range(stop): 0 to stop-1
for i in range(5):
    print(i)           # 0, 1, 2, 3, 4

# range(start, stop): inclusive start, exclusive stop
for i in range(2, 6):
    print(i)           # 2, 3, 4, 5

# range(start, stop, step): step controls increment
for i in range(0, 10, 2):
    print(i)           # 0, 2, 4, 6, 8

# Backwards
for i in range(5, 0, -1):
    print(i)           # 5, 4, 3, 2, 1
