# What you wrote:
if status_code == 401 or 403:  # ❌ Bug!
    print("auth error")

# Python sees: (status_code == 401) or (403, which is truthy!)
# This condition is ALWAYS True!
