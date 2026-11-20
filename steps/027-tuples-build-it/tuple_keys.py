# tuple_keys.py

# Tuple as a composite key
cache = {}
cache[("gpt-4", "en")] = "response in English"
cache[("claude-3", "fr")] = "réponse en français"

print(cache[("gpt-4", "en")])  # response in English

# List as key: fails
# cache[["gpt-4", "en"]] = "error"  # TypeError: unhashable type: 'list'
