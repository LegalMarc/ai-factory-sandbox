import json
import re
import sys


def main(argv, stdin, stdout):
    use_json = "--json" in argv
    text = stdin.read().lower()
    counts = {}
    for word in re.findall(r"[a-z0-9]+", text):
        counts[word] = counts.get(word, 0) + 1
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    total = sum(counts.values())
    if use_json:
        document = {
            "total": total,
            "words": [{"word": word, "count": count} for word, count in ordered],
        }
        stdout.write(json.dumps(document, indent=2) + "\n")
    else:
        for word, count in ordered:
            stdout.write("{} {}\n".format(word, count))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], sys.stdin, sys.stdout))
