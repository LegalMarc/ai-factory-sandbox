"""Command line interface for parsing and merging config files."""

import sys

from cfgparse import parse
from cfgmerge import merge


def main(argv, stdout):
    base_path, override_path = argv
    with open(base_path, "r") as handle:
        base = parse(handle.read())
    with open(override_path, "r") as handle:
        override = parse(handle.read())
    merged = merge(base, override)
    for key in sorted(merged):
        stdout.write("%s=%s\n" % (key, merged[key]))
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], sys.stdout))
