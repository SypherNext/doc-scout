import httpx

with httpx.Client() as client:
    response = client.get("https://httpbin.org/status/404")
    # Both work: httpx has the same API as requests here
    response.raise_for_status()  # Raises httpx.HTTPStatusError
