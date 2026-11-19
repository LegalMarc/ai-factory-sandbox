def parse(text):
    result = {}
    section = None
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line:
            continue
        if line.lstrip().startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1].strip()
            continue
        if "=" not in line:
            raise ValueError(f"invalid line: {raw_line!r}")
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if section:
            key = f"{section}.{key}"
        result[key] = value
    return result
