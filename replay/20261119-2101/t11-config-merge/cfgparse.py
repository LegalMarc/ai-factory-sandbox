def parse(text):
    result = {}
    section = None
    for line in text.splitlines():
        stripped = line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("["):
            if not stripped.endswith("]"):
                raise ValueError("invalid section line: " + line)
            section = stripped[1:-1].strip()
            continue
        if "=" not in line:
            raise ValueError("missing '=' in line: " + line)
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if section:
            key = section + "." + key
        result[key] = value
    return result
