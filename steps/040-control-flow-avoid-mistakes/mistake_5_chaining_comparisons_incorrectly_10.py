score = 0.45

# Bug: can any number be both > 0.6 AND < 0.3?
if 0.6 < score < 0.3:  # Always False, no number satisfies both
    print("in range")   # This never executes
