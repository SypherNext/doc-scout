import requests

# Creates a new TCP connection for every request: slow
for model in ["gpt-4", "claude-3", "llama-3"]:
    response = requests.post(
        "https://api.example.com/chat",
        json={"model": model, "prompt": "Hello"},
        headers={"Authorization": "Bearer ..."},
    )


with requests.Session() as session:
    session.headers.update({"Authorization": "Bearer ..."})
    for model in ["gpt-4", "claude-3", "llama-3"]:
        response = session.post(
            "https://api.example.com/chat",
            json={"model": model, "prompt": "Hello"},
        )
