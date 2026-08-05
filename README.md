# wordstats

A tiny word-frequency CLI. Counts tokens across text files and prints the most frequent.

```bash
wordstats notes.txt essay.txt --top 5
cat notes.txt | wordstats --top 5
```

```
total words:    128
distinct words: 61

top 5:
  the    9
  and    6
  a      4
  code   3
  test   3
```

## Options

| Flag | Meaning |
|---|---|
| `--top N` | how many of the most frequent words to show (default: 10) |
| `--min-length N` | ignore words shorter than N characters (default: 0, keep everything) |

## Layout

`wordstats/core.py` holds the pure functions — tokenizing, counting, ranking — and knows nothing
about files or arguments. `wordstats/cli.py` is a thin shell that reads input, calls those
functions, and formats the result. Tests cover the pure layer directly and the shell through
`main()`, so nothing needs a subprocess.

## Checks

```bash
python3 -m venv .venv && .venv/bin/pip install -q ruff pytest
bash scripts/check.sh
```

`scripts/check.sh` (ruff + pytest, fully offline) is the single source of truth and must be green.
It is the repo's control surface: a change that appears to need it relaxed is the wrong change.

## What this repo is for

A deliberately small, deliberately **public** practice target for an automated coding pipeline. It
holds nothing sensitive and never should — that is the point. Real code with real seams, small
enough that a job over it is cheap.
