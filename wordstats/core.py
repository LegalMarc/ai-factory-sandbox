"""Word statistics over text: tokenize, count, rank.

Pure functions only — no I/O, no argument parsing. Everything here is deterministic and directly
testable, which is what makes the CLI in `cli.py` a thin shell around it.
"""

from __future__ import annotations

import re
from collections import Counter

# A "word" is a run of letters, digits, apostrophes and hyphens. Deliberately simple: this is a
# sandbox, and a clever tokenizer would make the behaviour harder to reason about in a ticket.
WORD_RE = re.compile(r"[A-Za-z0-9]+(?:['\-][A-Za-z0-9]+)*")


def tokenize(text: str) -> list[str]:
    """Split `text` into lowercased word tokens, in order of appearance."""
    return [match.group(0).lower() for match in WORD_RE.finditer(text)]


def count_words(text: str) -> Counter[str]:
    """Frequency of every token in `text`."""
    return Counter(tokenize(text))


def filter_min_length(counts: Counter[str], min_length: int) -> Counter[str]:
    """Drop words shorter than `min_length`.

    `min_length <= 0` is a no-op: every word is at least one character, so there is nothing to
    filter and callers should not have to special-case it.
    """
    if min_length <= 0:
        return Counter(counts)
    return Counter({word: n for word, n in counts.items() if len(word) >= min_length})


def top_n(counts: Counter[str], n: int) -> list[tuple[str, int]]:
    """The `n` most frequent words, most frequent first.

    Ties are broken alphabetically so the output is stable across runs — `Counter.most_common`
    alone leaves tied entries in insertion order, which makes the CLI's output depend on where a
    word happened to appear in the input.
    """
    if n <= 0:
        return []
    ranked = sorted(counts.items(), key=lambda item: (-item[1], item[0]))
    return ranked[:n]


def total_words(counts: Counter[str]) -> int:
    """Total number of tokens counted (not the number of distinct words)."""
    return sum(counts.values())


def distinct_words(counts: Counter[str]) -> int:
    """Number of distinct words."""
    return len(counts)


def count_lines(text: str) -> int:
    """Number of non-empty lines in `text`; a line of only whitespace is empty."""
    return sum(1 for line in text.splitlines() if line.strip())


def count_chars(text: str) -> int:
    """Number of non-whitespace characters in `text`."""
    return sum(1 for char in text if not char.isspace())
