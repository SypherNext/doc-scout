# response_classifier.py: classify API responses by status and content

def classify_api_response(response):
    """
    Classify an API response dict into a summary status.

    Expected response format:
    {
        "status_code": int,
        "body": dict or None,
        "error": str or None,
    }
    """
    status = response.get("status_code", 0)
    body = response.get("body")
    error = response.get("error")

    # Determine the outcome
    if status >= 200 and status < 300:
        # Success, check body
        if body is None:
            return "success_empty_body"
        return "success"
    elif status == 429:
        return "rate_limited"
    elif status >= 500:
        if error and "timeout" in error.lower():
            return "timeout"
        return "server_error"
    elif status == 401 or status == 403:
        return "auth_error"
    elif error:
        return f"client_error: {error}"
    else:
        return "unknown"

responses = [
    {"status_code": 200, "body": {"result": "ok"}, "error": None},
    {"status_code": 429, "body": None, "error": "rate limit exceeded"},
    {"status_code": 503, "body": None, "error": "timeout upstream"},
    {"status_code": 401, "body": None, "error": "invalid API key"},
]

for resp in responses:
    status = classify_api_response(resp)
    print(f"Status {resp['status_code']} → {status}")
