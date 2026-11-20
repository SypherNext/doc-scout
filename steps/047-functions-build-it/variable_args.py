# variable_args.py

# *args: any number of positional arguments (collected as a tuple)
def calculate_total(*args):
    """Sum any number of values."""
    total = 0
    for value in args:
        total += value
    return total

print(calculate_total(1, 2, 3))           # 6
print(calculate_total(10, 20, 30, 40))    # 100

# **kwargs: any number of keyword arguments (collected as a dict)
def create_config(**kwargs):
    """Build a configuration dict from keyword arguments."""
    config = {
        "temperature": 0.7,
        "max_tokens": 1024,
        "top_p": 1.0,
    }
    config.update(kwargs)
    return config

config = create_config(model="gpt-4", temperature=0.3, max_tokens=4096)
print(config)
# {'temperature': 0.3, 'max_tokens': 4096, 'top_p': 1.0, 'model': 'gpt-4'}

# Combined
def wrapper_function(arg1, arg2, *args, **kwargs):
    """Demonstrate mixing positional, *args, and **kwargs."""
    print(f"arg1={arg1}, arg2={arg2}")
    print(f"extra positional: {args}")
    print(f"extra keyword: {kwargs}")

wrapper_function(1, 2, 3, 4, 5, key="value", debug=True)
# arg1=1, arg2=2
# extra positional: (3, 4, 5)
# extra keyword: {'key': 'value', 'debug': True}
