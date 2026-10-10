"""`wordstats` command line interface.

A thin shell around `wordstats.core`: read files, call pure functions, format output. Keeping the
logic out of here is what lets the test suite cover behaviour without spawning a process.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections.abc import Sequence
from pathlib import Path

from wordstats import core


def read_texts(paths: Sequence[str]) -> str:
    """Concatenate the contents of `paths`, or read stdin when no path is given.

    Files are read as UTF-8 with undecodable bytes replaced rather than raising: a stray byte in
    one input should not abort a word count over twenty files.
    """
    if not paths:
        return sys.stdin.read()
    chunks = []
    for path in paths:
        chunks.append(Path(path).read_text(encoding="utf-8", errors="replace"))
    return "\n".join(chunks)


def format_report(counts, top: int) -> str:
    """Human-readable report: totals, then the top-N table."""
    lines = [
        f"total words:    {core.total_words(counts)}",
        f"distinct words: {core.distinct_words(counts)}",
        "",
    ]
    ranked = core.top_n(counts, top)
    if not ranked:
        lines.append("(no words)")
        return "\n".join(lines)

    width = max(len(word) for word, _ in ranked)
    lines.append(f"top {len(ranked)}:")
    for word, n in ranked:
        lines.append(f"  {word.ljust(width)}  {n}")
    return "\n".join(lines)


def format_json_report(counts, top: int) -> str:
    """JSON report with totals and the top-N ranking."""
    report = {
        "total_words": core.total_words(counts),
        "distinct_words": core.distinct_words(counts),
        "top": [{"word": word, "count": n} for word, n in core.top_n(counts, top)],
    }
    return json.dumps(report)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="wordstats",
        description="Count word frequencies across text files.",
    )
    parser.add_argument("paths", nargs="*", help="text files to read (default: stdin)")
    parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="how many of the most frequent words to show (default: 10)",
    )
    parser.add_argument(
        "--min-length",
        type=int,
        default=0,
        help="ignore words shorter than this many characters (default: 0, keep everything)",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="format the report as JSON",
    )
    parser.add_argument(
        "--total-only",
        action="store_true",
        help="print only the total word count as a bare integer",
    )
    parser.add_argument(
        "--lines",
        action="store_true",
        help="print only the number of non-empty lines as a bare integer",
    )
    parser.add_argument(
        "--chars",
        action="store_true",
        help="print only the number of non-whitespace characters as a bare integer",
    )
    parser.add_argument(
        "--longest",
        action="store_true",
        help="print the length of the longest whitespace-separated word as a bare integer",
    )
    return parser


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        text = read_texts(args.paths)
    except OSError as exc:
        print(f"wordstats: {exc}", file=sys.stderr)
        return 2

    counts = core.count_words(text)
    counts = core.filter_min_length(counts, args.min_length)
    if args.lines:
        print(core.count_lines(text))
        return 0
    if args.chars:
        print(core.count_chars(text))
        return 0
    if args.longest:
        print(core.longest_word(text))
        return 0
    if args.total_only:
        print(core.total_words(counts))
        return 0
    report = format_json_report(counts, args.top) if args.json else format_report(counts, args.top)
    print(report)
    return 0


if __name__ == "__main__":  # pragma: no cover
    raise SystemExit(main())
