import json

# Simulated API response (what an LLM provider returns)
api_response = """
{
  "id": "chatcmpl-abc123",
  "object": "chat.completion",
  "created": 1718000000,
  "model": "gpt-4",
  "choices": [
    {
      "index": 0,
      "message": {
        "role": "assistant",
        "content": "The capital of France is Paris."
      },
      "finish_reason": "stop"
    }
  ],
  "usage": {
    "prompt_tokens": 14,
    "completion_tokens": 7,
    "total_tokens": 21
  }
}
"""

parsed = json.loads(api_response)

# Navigate nested structure
content = parsed["choices"][0]["message"]["content"]
print(content)  # The capital of France is Paris.

tokens = parsed["usage"]["total_tokens"]
print(f"Total tokens: {tokens}")  # Total tokens: 21

model = parsed["model"]
print(f"Model: {model}")  # Model: gpt-4
