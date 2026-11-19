import re
from collections import Counter


def top_words(text, n=3, stopwords=()):
    if n <= 0:
        return []
    stop = {str(s).lower() for s in stopwords}
    words = re.findall(r"[a-z0-9]+", text.lower())
    words = [w for w in words if w not in stop]
    counts = Counter(words)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ordered[:n]
