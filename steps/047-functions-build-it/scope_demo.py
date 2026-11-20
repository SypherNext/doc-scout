# scope_demo.py

model_name = "gpt-4"  # Global scope

def run_inference():
    model_name = "claude-3"  # Local scope: shadows the global
    print(f"Inside function: {model_name}")

run_inference()  # Inside function: claude-3
print(f"Outside function: {model_name}")  # Outside function: gpt-4

# To modify a global variable inside a function, use 'global' (rarely needed)
counter = 0

def increment():
    global counter
    counter += 1

increment()
print(counter)  # 1

# Better approach: pass and return
counter = 0

def increment(c):
    return c + 1

counter = increment(counter)
print(counter)  # 1
