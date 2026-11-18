import sys

from cfgmerge import merge
from cfgparse import parse


def main(argv, stdout):
    with open(argv[0]) as f:
        base = parse(f.read())
    with open(argv[1]) as f:
        override = parse(f.read())
    merged = merge(base, override)
    for key in sorted(merged):
        stdout.write("%s=%s\n" % (key, merged[key]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], sys.stdout))
