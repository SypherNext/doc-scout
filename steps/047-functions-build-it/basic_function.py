# basic_function.py

def greet(name):
    """Return a personalised greeting string."""
    return f"Hello, {name}! Welcome to the AI course."

# Call the function
message = greet("Alice")
print(message)  # Hello, Alice! Welcome to the AI course.

# A function without return returns None
def log_progress(step):
    print(f"Completed step {step}")

result = log_progress(3)
print(result)  # None
