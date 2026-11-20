def add_defaults(config):
    config = config.copy()  # Work on a copy
    config["temperature"] = 0.7
    config["max_tokens"] = 1024
    return config
