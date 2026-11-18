import json
import re
import sys
from collections import Counter


def main(argv, stdin, stdout):
    counts = Counter(re.findall(r"[a-z0-9]+", stdin.read().lower()))
    total = sum(counts.values())
    words = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    if "--json" in argv:
        document = {
            "total": total,
            "words": [{"word": word, "count": count} for word, count in words],
        }
        stdout.write(json.dumps(document, indent=2) + "\n")
    else:
        for word, count in words:
            stdout.write(f"{word} {count}\n")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], sys.stdin, sys.stdout))
