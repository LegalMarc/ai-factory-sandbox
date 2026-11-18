"""Parse simple key = value configuration text."""


def parse(text):
    result = {}
    section = None
    for raw in text.splitlines():
        line = raw.strip()
        if not line or line.startswith("#"):
            continue
        if line.startswith("[") and line.endswith("]"):
            section = line[1:-1].strip()
            continue
        if "=" not in line:
            raise ValueError("missing '=' in line: %r" % raw)
        key, value = line.split("=", 1)
        key = key.strip()
        value = value.strip()
        if section is not None:
            key = section + "." + key
        result[key] = value
    return result
