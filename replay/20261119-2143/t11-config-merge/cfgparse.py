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
        if "=" not in raw_line:
            raise ValueError(f"invalid line: {raw_line!r}")
        key, _, value = raw_line.partition("=")
        key = key.strip()
        value = value.strip()
        if section:
            key = f"{section}.{key}"
        result[key] = value
    return result
