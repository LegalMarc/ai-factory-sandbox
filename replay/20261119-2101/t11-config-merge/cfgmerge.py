def merge(base, override):
    result = dict(base)
    for key, value in override.items():
        if value == "":
            result.pop(key, None)
        else:
            result[key] = value
    return result
