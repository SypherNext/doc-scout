def describe(confidence):
    if confidence > 0.3:
        return "medium"
    elif confidence > 0.6:  # This branch can never execute!
        return "high"
    else:
        return "low"

print(describe(0.8))  # "medium", not "high"!
