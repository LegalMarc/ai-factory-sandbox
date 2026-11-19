import json
import re
import sys


def main(argv, stdin, stdout):
    text = stdin.read().lower()
    words = re.findall(r"[a-z0-9]+", text)

    counts = {}
    for word in words:
        counts[word] = counts.get(word, 0) + 1

    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))

    if "--json" in argv:
        data = {
            "total": len(words),
            "words": [{"word": word, "count": count} for word, count in ordered],
        }
        stdout.write(json.dumps(data, indent=2) + "\n")
    else:
        for word, count in ordered:
            stdout.write("%s %d\n" % (word, count))

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], sys.stdin, sys.stdout))
