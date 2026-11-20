for key in list(config.keys()):
    if key.startswith("max_"):
        del config[key]
