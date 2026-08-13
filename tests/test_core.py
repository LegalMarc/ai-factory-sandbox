"""Tests for the pure functions in `wordstats.core`."""

from __future__ import annotations

from collections import Counter

from wordstats import core


def test_tokenize_lowercases_and_splits_on_punctuation():
    assert core.tokenize("The cat, the HAT!") == ["the", "cat", "the", "hat"]


def test_tokenize_keeps_internal_apostrophes_and_hyphens():
    assert core.tokenize("it's well-known") == ["it's", "well-known"]


def test_tokenize_ignores_surrounding_punctuation():
    assert core.tokenize("--well-known--") == ["well-known"]


def test_tokenize_empty_text():
    assert core.tokenize("") == []


def test_count_words_counts_repeats():
    assert core.count_words("a b a c a") == Counter({"a": 3, "b": 1, "c": 1})


def test_top_n_orders_by_frequency():
    counts = Counter({"a": 5, "b": 3, "c": 1})
    assert core.top_n(counts, 2) == [("a", 5), ("b", 3)]


def test_top_n_breaks_ties_alphabetically():
    """Stable output matters: without this the CLI's ordering depends on input order."""
    counts = Counter({"pear": 2, "apple": 2, "fig": 2})
    assert core.top_n(counts, 3) == [("apple", 2), ("fig", 2), ("pear", 2)]


def test_top_n_returns_everything_when_n_exceeds_vocabulary():
    counts = Counter({"a": 2, "b": 1})
    assert core.top_n(counts, 99) == [("a", 2), ("b", 1)]


def test_top_n_of_zero_or_negative_is_empty():
    counts = Counter({"a": 2})
    assert core.top_n(counts, 0) == []
    assert core.top_n(counts, -1) == []


def test_filter_min_length_of_zero_is_a_no_op():
    counts = Counter({"a": 1, "bb": 2})
    assert core.filter_min_length(counts, 0) == counts


def test_filter_min_length_does_not_mutate_its_input():
    counts = Counter({"a": 1, "bbbb": 2})
    core.filter_min_length(counts, 2)
    assert counts == Counter({"a": 1, "bbbb": 2})


def test_filter_stopwords_excludes_listed_words():
    counts = Counter({"the": 3, "cat": 2, "sat": 1})
    assert core.filter_stopwords(counts, {"the"}) == Counter({"cat": 2, "sat": 1})


def test_filter_stopwords_is_case_insensitive():
    counts = Counter({"the": 3, "cat": 2})
    assert core.filter_stopwords(counts, {"The"}) == Counter({"cat": 2})


def test_filter_stopwords_and_min_length_combine_regardless_of_order():
    base = Counter({"the": 3, "a": 1, "cat": 2, "sat": 1})
    a = core.filter_min_length(core.filter_stopwords(Counter(base), {"the"}), 1)
    b = core.filter_stopwords(core.filter_min_length(Counter(base), 1), {"the"})
    assert a == b == Counter({"cat": 2, "sat": 1})


def test_totals():
    counts = core.count_words("a b a")
    assert core.total_words(counts) == 3
    assert core.distinct_words(counts) == 2


def test_totals_of_empty_input():
    counts = core.count_words("")
    assert core.total_words(counts) == 0
    assert core.distinct_words(counts) == 0
