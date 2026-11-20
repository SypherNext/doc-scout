import json

data = "{'model': 'gpt-4'}"  # Not valid JSON!

try:
    parsed = json.loads(data)  # Raises json.JSONDecodeError
except json.JSONDecodeError as e:
    print(e)  # Expecting property name enclosed in double quotes
