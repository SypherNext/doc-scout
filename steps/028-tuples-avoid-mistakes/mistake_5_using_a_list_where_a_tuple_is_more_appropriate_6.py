# Over-use of lists: this should be a tuple
def get_config():
    return ["gpt-4", 2026, True]  # Returns a mutable list for a fixed record

config = get_config()
config.append("extra")  # This should not be possible for a fixed record
