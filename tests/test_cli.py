"""Tests for the `wordstats` CLI shell."""

from __future__ import annotations

from collections import Counter

from wordstats import cli


def test_read_texts_concatenates_files(tmp_path):
    a = tmp_path / "a.txt"
    b = tmp_path / "b.txt"
    a.write_text("alpha beta")
    b.write_text("gamma")
    assert cli.read_texts([str(a), str(b)]) == "alpha beta\ngamma"


def test_read_texts_reads_stdin_when_no_paths(monkeypatch):
    import io

    monkeypatch.setattr("sys.stdin", io.StringIO("from stdin"))
    assert cli.read_texts([]) == "from stdin"


def test_read_texts_replaces_undecodable_bytes(tmp_path):
    """One stray byte must not abort a count over many files."""
    path = tmp_path / "bad.txt"
    path.write_bytes(b"caf\xff hello")
    assert "hello" in cli.read_texts([str(path)])


def test_format_report_includes_totals_and_ranking():
    counts = Counter({"apple": 3, "fig": 1})
    report = cli.format_report(counts, top=10)
    assert "total words:    4" in report
    assert "distinct words: 2" in report
    assert "apple" in report and "fig" in report


def test_format_report_on_empty_input():
    assert "(no words)" in cli.format_report(Counter(), top=10)


def test_main_happy_path(tmp_path, capsys):
    path = tmp_path / "in.txt"
    path.write_text("red green red blue red green")
    assert cli.main([str(path)]) == 0
    out = capsys.readouterr().out
    assert "total words:    6" in out
    assert "red" in out


def test_main_respects_top(tmp_path, capsys):
    path = tmp_path / "in.txt"
    path.write_text("a a a b b c")
    assert cli.main([str(path), "--top", "1"]) == 0
    out = capsys.readouterr().out
    assert "top 1:" in out
    assert "\n  b" not in out


def test_main_reports_a_missing_file_without_a_traceback(tmp_path, capsys):
    assert cli.main([str(tmp_path / "nope.txt")]) == 2
    assert "wordstats:" in capsys.readouterr().err
