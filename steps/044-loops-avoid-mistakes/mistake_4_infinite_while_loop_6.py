# Bug: never decreases, so the condition is always True
x = 10
while x > 0:
    print(x)
    # forgot: x -= 1
