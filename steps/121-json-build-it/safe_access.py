import json

response = json.loads('{"id": "123", "choices": []}')

# Unsafe: KeyError if key is missing
# content = response["choices"][0]["message"]["content"]

# Safe: .get() with defaults
# Note: the default argument to .get() only kicks in when the key is
# MISSING, not when it's present but falsy (like an empty list), so
# "choices" or [{}] is needed to cover both cases.
choices = response.get("choices") or [{}]
content = choices[0].get("message", {}).get("content", "no content")
print(content)  # no content

# Or check the structure explicitly
if response.get("choices") and len(response["choices"]) > 0:
    first_choice = response["choices"][0]
    if "message" in first_choice and "content" in first_choice["message"]:
        content = first_choice["message"]["content"]
    else:
        content = "no content"
else:
    content = "no content"
