# ternary_demo.py

# Instead of:
if confidence > 0.5:
    label = "positive"
else:
    label = "negative"

# Write:
label = "positive" if confidence > 0.5 else "negative"

# Nesting ternaries, avoid for complex logic
# "high" if > 0.8, "medium" if > 0.4, "low" otherwise
level = "high" if confidence > 0.8 else ("medium" if confidence > 0.4 else "low")
