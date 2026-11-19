import sys
from cfgparse import parse
from cfgmerge import merge


def main(argv, stdout):
    with open(argv[0], "r", encoding="utf-8") as f:
        base = parse(f.read())
    with open(argv[1], "r", encoding="utf-8") as f:
        override = parse(f.read())
    merged = merge(base, override)
    for key in sorted(merged):
        stdout.write(key + "=" + merged[key] + "\n")
    return 0


if __name__ == "__main__":
    main(sys.argv[1:], sys.stdout)
