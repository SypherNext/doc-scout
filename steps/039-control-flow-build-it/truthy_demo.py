# truthy_demo.py
def is_valid_response(response):
    """Check if a response has meaningful content."""
    # None, empty string, empty list/dict all return False
    if not response:
        return False
    return True

print(is_valid_response(None))          # False
print(is_valid_response(""))            # False
print(is_valid_response([]))            # False
print(is_valid_response("Hello"))       # True
print(is_valid_response(["result"]))    # True
print(is_valid_response(0))             # False
print(is_valid_response(1))             # True
