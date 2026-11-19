import sys

import cfgparse
import cfgmerge


def main(argv, stdout):
    base_path, override_path = argv[0], argv[1]
    with open(base_path) as f:
        base_text = f.read()
    with open(override_path) as f:
        override_text = f.read()
    base = cfgparse.parse(base_text)
    override = cfgparse.parse(override_text)
    merged = cfgmerge.merge(base, override)
    for key in sorted(merged):
        stdout.write(f"{key}={merged[key]}\n")
    return 0


if __name__ == "__main__":
    main(sys.argv[1:], sys.stdout)
