# casting_demo.py

# String to integer
age_str = "25"
age = int(age_str)
print(age + 1)  # 26: works because age is now an int

# Integer to string
score = 98
message = "Score: " + str(score)
print(message)  # Score: 98

# String to float
rate = float("0.85")
print(rate * 100)  # 85.0

# Anything to boolean
print(bool(1))      # True
print(bool(0))      # False
print(bool(""))     # False: empty string is falsy
print(bool("hi"))   # True: non-empty string is truthy
print(bool(None))   # False: None is always falsy
