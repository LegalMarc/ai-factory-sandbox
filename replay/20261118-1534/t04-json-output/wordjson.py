import json
import re
import sys


def _count_words(text):
    counts = {}
    for word in re.findall("[a-z0-9]+", text.lower()):
        counts[word] = counts.get(word, 0) + 1
    return counts


def main(argv, stdin, stdout):
    counts = _count_words(stdin.read())
    ordered = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    if "--json" in argv:
        document = {
            "total": sum(counts.values()),
            "words": [{"word": word, "count": count} for word, count in ordered],
        }
        stdout.write(json.dumps(document, indent=2) + "\n")
    else:
        for word, count in ordered:
            stdout.write("%s %d\n" % (word, count))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], sys.stdin, sys.stdout))
