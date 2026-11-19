import sys

from cfgparse import parse
from cfgmerge import merge


def main(argv, stdout):
    base_path, override_path = argv
    with open(base_path) as f:
        base = parse(f.read())
    with open(override_path) as f:
        override = parse(f.read())
    result = merge(base, override)
    for key in sorted(result):
        stdout.write(f"{key}={result[key]}\n")
    return 0


if __name__ == "__main__":
    main(sys.argv[1:], sys.stdout)
