import re
import unicodedata


def slugify(text):
    normalized = unicodedata.normalize("NFKD", text)
    stripped = "".join(c for c in normalized if not unicodedata.combining(c)).lower()
    return re.sub(r"[^a-z0-9]+", "-", stripped).strip("-")
