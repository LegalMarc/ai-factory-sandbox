import re
import unicodedata


def slugify(text):
    if not text:
        return ""
    normalized = unicodedata.normalize("NFKD", text)
    without_marks = "".join(c for c in normalized if not unicodedata.combining(c))
    lowered = without_marks.lower()
    slug = re.sub(r"[^a-z0-9]+", "-", lowered)
    return slug.strip("-")
