import re
import unicodedata


def slugify(text):
    normalized = unicodedata.normalize("NFKD", text)
    without_marks = "".join(
        c for c in normalized if not unicodedata.category(c).startswith("M")
    )
    return re.sub(r"[^a-z0-9]+", "-", without_marks.lower()).strip("-")
