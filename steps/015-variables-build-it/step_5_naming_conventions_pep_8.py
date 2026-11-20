# ✅ Good: snake_case for variables and functions
model_name = "gpt-4"
batch_size = 32
learning_rate = 0.001

# ✅ Good: UPPER_CASE for constants
MAX_RETRIES = 3
API_ENDPOINT = "https://api.example.com"

# ✅ Good: leading underscore for internal / private use
_internal_cache = {}

# ❌ Bad: camelCase (used in JavaScript but not Python)
modelName = "gpt-4"      # Avoid

# ❌ Bad: single-letter names (except in loops)
x = "some value"          # Avoid: what is x?

# ❌ Bad: names that shadow built-ins
list = [1, 2, 3]          # Avoid: overrides the list() built-in
