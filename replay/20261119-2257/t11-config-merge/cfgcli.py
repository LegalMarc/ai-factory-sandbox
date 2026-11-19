import sys

from cfgmerge import merge
from cfgparse import parse


def main(argv, stdout):
    base_path, override_path = argv[0], argv[1]
    with open(base_path) as f:
        base = parse(f.read())
    with open(override_path) as f:
        override = parse(f.read())
    merged = merge(base, override)
    for key in sorted(merged):
        stdout.write(f"{key}={merged[key]}\n")
    return 0


if __name__ == "__main__":
    main(sys.argv[1:], sys.stdout)
