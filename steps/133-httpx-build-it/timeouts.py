import httpx

# Single timeout value (connect + read + write + pool)
with httpx.Client(timeout=10.0) as client:
    response = client.get("https://httpbin.org/delay/1")
    print(f"OK: {response.status_code}")  # 200

# Per-operation timeouts
timeout = httpx.Timeout(
    connect=3.0,    # Time to establish connection
    read=10.0,      # Time to receive response body
    write=5.0,      # Time to send request body
    pool=30.0,      # Time to wait for a connection from pool
)

with httpx.Client(timeout=timeout) as client:
    response = client.get("https://httpbin.org/get")
    print(f"Granular timeout: {response.status_code}")

    # Per-request override: still inside the `with` block, before the
    # client closes. A client only accepts requests while it is open.
    response = client.get("https://httpbin.org/delay/5", timeout=30.0)
    print(f"Per-request override: {response.status_code}")
