import re
import unicodedata


def slugify(text):
    normalized = unicodedata.normalize("NFKD", text)
    chars = []
    for ch in normalized:
        if "a" <= ch <= "z" or "0" <= ch <= "9":
            chars.append(ch)
        elif "A" <= ch <= "Z":
            chars.append(ch.lower())
        elif unicodedata.category(ch).startswith("M"):
            continue
        else:
            chars.append("-")
    return re.sub(r"[^a-z0-9]+", "-", "".join(chars)).strip("-")
