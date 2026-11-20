# match_demo.py

def route_model(model_name):
    """Route a model name to its provider API."""
    match model_name:
        case "gpt-4" | "gpt-3.5-turbo":
            return "https://api.openai.com/v1/chat/completions"
        case "claude-3-opus" | "claude-3-sonnet":
            return "https://api.anthropic.com/v1/messages"
        case "llama-3":
            return "https://api.groq.com/openai/v1/chat/completions"
        case _:
            return "unknown_provider"

print(route_model("gpt-4"))          # https://api.openai.com/v1/chat/completions
print(route_model("claude-3-opus"))   # https://api.anthropic.com/v1/messages
print(route_model("fictional-model")) # unknown_provider
