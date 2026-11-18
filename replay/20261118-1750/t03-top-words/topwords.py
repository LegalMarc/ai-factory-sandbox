import re
from collections import Counter


def top_words(text, n=3, stopwords=()):
    if n <= 0:
        return []
    words = re.findall(r"[a-z0-9]+", text.lower())
    stop = {word.lower() for word in stopwords}
    counts = Counter(word for word in words if word not in stop)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:n]
