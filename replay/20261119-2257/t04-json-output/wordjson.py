import json
import re
import sys
from collections import Counter


def main(argv, stdin, stdout):
    use_json = "--json" in (argv or [])
    text = stdin.read()
    words = re.findall(r"[a-z0-9]+", text.lower())
    counts = Counter(words)
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    total = len(words)
    if use_json:
        obj = {"total": total, "words": [{"word": word, "count": count} for word, count in ordered]}
        stdout.write(json.dumps(obj, indent=2) + "\n")
    else:
        for word, count in ordered:
            stdout.write(f"{word} {count}\n")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], sys.stdin, sys.stdout))
