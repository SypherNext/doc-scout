# parameters.py

# Positional arguments: order matters
def build_prompt(system_msg, user_msg, example=None):
    prompt = f"System: {system_msg}\n\n"
    if example:
        prompt += f"Example: {example}\n\n"
    prompt += f"User: {user_msg}"
    return prompt

print(build_prompt("You are helpful.", "Tell me a joke."))

# Keyword arguments: specify by name, order does not matter
print(build_prompt(
    user_msg="Tell me a joke.",
    system_msg="You are helpful.",
    example="Q: Why did the chicken cross the road? A: To get to the other side.",
))

# Default parameter values: example defaults to None
print(build_prompt("You are helpful.", "Tell me a joke."))
