# Wrong, visible to everyone with repo access
API_KEY = "sk-abc123def456ghi789"

# Wrong, committed to version control
# config.py: API_KEY = "sk-..."


import os
API_KEY = os.environ["OPENAI_API_KEY"]  # Raises KeyError if not set
