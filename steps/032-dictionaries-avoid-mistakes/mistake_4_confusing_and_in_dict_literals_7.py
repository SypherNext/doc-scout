# ❌ SyntaxError: dict literal uses : not =
# {"model" = "gpt-4"}

# ✅ Correct
{"model": "gpt-4"}

# dict() constructor with keyword args: keys are strings without quotes
dict(model="gpt-4", temperature=0.7)
