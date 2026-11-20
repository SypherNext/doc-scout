import requests

# Stream a response: useful for large payloads or SSE
with requests.get(
    "https://httpbin.org/stream/5",  # Streams 5 lines
    stream=True,
) as response:
    for line in response.iter_lines():
        if line:
            print(line.decode("utf-8"))
