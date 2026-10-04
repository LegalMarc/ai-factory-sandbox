"""Allow `python -m wordstats` to run the CLI."""

from wordstats.cli import main

if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
