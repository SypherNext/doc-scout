import json

untrusted = '{"choices": null}'
parsed = json.loads(untrusted)

# This will crash
first = parsed["choices"][0]  # TypeError: 'NoneType' object is not subscriptable


choices = parsed.get("choices")
if choices and isinstance(choices, list) and len(choices) > 0:
    content = choices[0].get("message", {}).get("content")
