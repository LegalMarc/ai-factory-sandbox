import sys

from cfgparse import parse
from cfgmerge import merge


def main(argv, stdout):
    base_path, override_path = argv[0], argv[1]
    with open(base_path, "r", encoding="utf-8") as f:
        base_text = f.read()
    with open(override_path, "r", encoding="utf-8") as f:
        override_text = f.read()
    merged = merge(parse(base_text), parse(override_text))
    for key in sorted(merged):
        stdout.write(f"{key}={merged[key]}\n")
    return 0


if __name__ == "__main__":
    main(sys.argv[1:], sys.stdout)
