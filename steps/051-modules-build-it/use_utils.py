# use_utils.py: Imports from ai_utils.py
import ai_utils

text = "Python modules are useful for organising code. " * 100

blocks = ai_utils.split_fixed_width(text, max_chars=200)
print(f"Split into {len(blocks)} blocks")

token_estimate = ai_utils.count_tokens(text)
print(f"Approximate tokens: {token_estimate}")

shortened = ai_utils.truncate_to_max_tokens(text, max_tokens=50)
print(f"Truncated: {shortened[:50]}...")
