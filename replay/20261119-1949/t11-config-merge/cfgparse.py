def parse(text):
    result = {}
    section = None
    for raw_line in text.splitlines():
        stripped = raw_line.strip()
        if not stripped:
            continue
        if stripped.startswith("#"):
            continue
        if stripped.startswith("[") and stripped.endswith("]"):
            section = stripped[1:-1].strip()
            continue
        if "=" not in stripped:
            raise ValueError(f"invalid line: {raw_line!r}")
        key, value = stripped.split("=", 1)
        key = key.strip()
        value = value.strip()
        if section:
            full_key = f"{section}.{key}"
        else:
            full_key = key
        result[full_key] = value
    return result
