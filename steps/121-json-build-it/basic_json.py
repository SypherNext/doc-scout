import json

# Python dict → JSON string (serialize)
data = {
    "model": "gpt-4",
    "temperature": 0.7,
    "max_tokens": 2048,
    "stream": False,
    "stop": None,
}

json_str = json.dumps(data, indent=2)
print(json_str)
# {
#   "model": "gpt-4",
#   "temperature": 0.7,
#   "max_tokens": 2048,
#   "stream": false,
#   "stop": null
# }

# JSON string → Python dict (deserialize)
parsed = json.loads(json_str)
print(parsed["model"])        # gpt-4
print(type(parsed["stream"])) # <class 'bool'>
print(parsed["stop"])         # None
