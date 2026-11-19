import re
import unicodedata


def slugify(text):
    normalized = unicodedata.normalize("NFKD", text).lower()
    stripped = "".join(char for char in normalized if not unicodedata.combining(char))
    slug = re.sub(r"[^a-z0-9]+", "-", stripped)
    return slug.strip("-")
