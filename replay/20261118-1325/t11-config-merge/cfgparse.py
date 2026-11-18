def parse(text):
    result = {}
    section = ""
    for raw_line in text.splitlines():
        line = raw_line.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1].strip()
            continue
        if "=" not in line:
            raise ValueError("missing '=' in line: %r" % raw_line)
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if section:
            key = section + "." + key
        result[key] = value
    return result
