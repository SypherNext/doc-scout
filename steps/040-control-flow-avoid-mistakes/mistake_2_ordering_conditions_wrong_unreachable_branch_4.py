if confidence > 0.6:
    return "high"
elif confidence > 0.3:
    return "medium"
else:
    return "low"
