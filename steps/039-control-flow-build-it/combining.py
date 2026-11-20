# combining.py

def should_retry(status_code, retries_left, is_idempotent):
    """Determine if a failed API call should be retried."""
    if (status_code >= 500 or status_code == 429) and retries_left > 0:
        return True

    if status_code == 408 and retries_left > 0 and is_idempotent:
        return True

    return False

print(should_retry(503, 3, True))   # True, server error, retries available
print(should_retry(429, 0, True))   # False, no retries left
print(should_retry(408, 2, False))  # False, not idempotent
print(should_retry(400, 3, True))   # False, client error (4xx), don't retry

# Use parentheses for clarity, even when Python's precedence would work
# Without parens: `status_code >= 500 or status_code == 429 and retries_left > 0`
# `and` binds tighter than `or`, so the above means status_code >= 500 OR (status_code == 429 AND retries_left > 0)
# The parentheses here change the meaning: (status_code >= 500 OR status_code == 429) AND retries_left > 0
