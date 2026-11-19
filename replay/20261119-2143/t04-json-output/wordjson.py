import json
import re
import sys
from collections import Counter

WORD_RE = re.compile(r"[a-z0-9]+")


def main(argv, stdin, stdout):
    use_json = "--json" in argv[1:]
    text = stdin.read().lower()
    words = WORD_RE.findall(text)
    counts = Counter(words)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    if use_json:
        doc = {
            "total": len(words),
            "words": [{"word": w, "count": c} for w, c in ordered],
        }
        stdout.write(json.dumps(doc, indent=2) + "\n")
    else:
        for word, count in ordered:
            stdout.write(f"{word} {count}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv, sys.stdin, sys.stdout))
