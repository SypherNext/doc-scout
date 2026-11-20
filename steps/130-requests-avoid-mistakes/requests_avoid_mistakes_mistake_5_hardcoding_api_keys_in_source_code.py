# Wrong: key visible in source control
API_KEY = "sk-abc123..."

# Wrong: key in a config file committed to git
# config.json: {"api_key": "sk-abc123..."}


import os

API_KEY = os.environ.get("OPENAI_API_KEY")
if not API_KEY:
    raise ValueError("OPENAI_API_KEY environment variable is not set")
