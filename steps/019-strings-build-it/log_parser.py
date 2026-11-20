# log_parser.py: Extract fields from structured log lines

def parse_log_line(line):
    """Parse a structured log line into its components."""
    line = line.strip()
    if not line:
        return None

    # Split by whitespace: LEVEL DATE TIME key=value ...
    parts = line.split()

    level = parts[0]
    date = parts[1]
    time = parts[2]

    # Remaining parts are key=value pairs
    fields = {}
    for pair in parts[3:]:
        key, value = pair.split("=")
        fields[key] = value

    return {
        "level": level,
        "date": date,
        "time": time,
        "fields": fields,
    }

log_line = "INFO 2026-06-30 14:30:22 model=gpt-4 tokens=150 latency=2342ms"
result = parse_log_line(log_line)
print(result["level"])          # INFO
print(result["fields"]["model"])      # gpt-4
print(result["fields"]["tokens"])     # 150
print(result["fields"]["latency"])    # 2342ms

# ---

def build_prompt(system_message, user_message, examples=None):
    """Build a chat prompt from components."""
    parts = [f"System: {system_message}"]

    if examples:
        for ex in examples:
            parts.append(f"Example: {ex}")

    parts.append(f"User: {user_message}")
    return "\n\n".join(parts)

prompt = build_prompt(
    "You are a helpful assistant.",
    "Explain Python strings.",
    ["Example 1: Slicing", "Example 2: f-strings"],
)
print(prompt)
# System: You are a helpful assistant.
#
# Example: Example 1: Slicing
#
# Example: Example 2: f-strings
#
# User: Explain Python strings.
