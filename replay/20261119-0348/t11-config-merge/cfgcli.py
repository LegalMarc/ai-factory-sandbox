import sys

from cfgparse import parse
from cfgmerge import merge


def main(argv, stdout):
    with open(argv[0], encoding="utf-8") as handle:
        base = parse(handle.read())
    with open(argv[1], encoding="utf-8") as handle:
        override = parse(handle.read())
    result = merge(base, override)
    for key in sorted(result):
        stdout.write("%s=%s\n" % (key, result[key]))
    return 0


if __name__ == "__main__":
    main(sys.argv[1:], sys.stdout)
