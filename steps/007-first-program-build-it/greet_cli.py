# greet_cli.py: Reads a name from the command line
import sys

# sys.argv is a list: [script_name, arg1, arg2, ...]
if len(sys.argv) < 2:
    print("Usage: python3 greet_cli.py <name>")
    sys.exit(1)

name = sys.argv[1]
message = "Hello, " + name + "! Welcome to Python for AI."
print(message)
