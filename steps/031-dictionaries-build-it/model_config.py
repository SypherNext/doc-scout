# model_config.py: Manage model configurations

from collections import defaultdict

# Default configuration for any model
DEFAULT_CONFIG = {
    "temperature": 0.7,
    "max_tokens": 1024,
    "top_p": 1.0,
    "frequency_penalty": 0.0,
    "presence_penalty": 0.0,
    "stop": [],
}

def create_model_config(model_name, overrides=None):
    """Create a model configuration, merging defaults with overrides."""
    config = DEFAULT_CONFIG.copy()
    config["model"] = model_name
    if overrides:
        config.update(overrides)
    return config

# Create specific configurations
gpt4_config = create_model_config("gpt-4", {
    "temperature": 0.3,
    "max_tokens": 4096,
})
claude_config = create_model_config("claude-3-opus", {
    "temperature": 0.5,
    "max_tokens": 8192,
    "top_p": 0.9,
})

print(gpt4_config)
print(claude_config)

# ---

# Process API response (like what you would get from OpenAI)

def process_api_response(response):
    """Extract key fields from an API response dict."""
    return {
        "content": response["choices"][0]["message"]["content"],
        "model": response["model"],
        "prompt_tokens": response["usage"]["prompt_tokens"],
        "completion_tokens": response["usage"]["completion_tokens"],
        "total_tokens": response["usage"]["total_tokens"],
        "finish_reason": response["choices"][0]["finish_reason"],
    }

# Simulated API response
api_response = {
    "id": "chatcmpl-123",
    "model": "gpt-4",
    "choices": [
        {
            "message": {
                "role": "assistant",
                "content": "Python dictionaries are key-value stores.",
            },
            "finish_reason": "stop",
        }
    ],
    "usage": {
        "prompt_tokens": 25,
        "completion_tokens": 8,
        "total_tokens": 33,
    },
}

parsed = process_api_response(api_response)
print(f"Response: {parsed['content']}")
print(f"Total tokens used: {parsed['total_tokens']}")  # 33
