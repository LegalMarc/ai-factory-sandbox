import sys

from cfgmerge import merge
from cfgparse import parse


def main(argv, stdout):
    base_path, override_path = argv[0], argv[1]
    with open(base_path, encoding="utf-8") as handle:
        base = parse(handle.read())
    with open(override_path, encoding="utf-8") as handle:
        override = parse(handle.read())
    merged = merge(base, override)
    for key in sorted(merged):
        stdout.write("%s=%s\n" % (key, merged[key]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], sys.stdout))
