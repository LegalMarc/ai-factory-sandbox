import io
import os
import tempfile
import unittest

from cfgparse import parse
from cfgmerge import merge
from cfgcli import main


class TestCfgParse(unittest.TestCase):
    def test_parse_basic(self):
        self.assertEqual(parse("a = 1\nb=2\n"), {"a": "1", "b": "2"})

    def test_parse_comments_and_blank(self):
        self.assertEqual(parse("# c\n\n  # indented\na = 1\n"), {"a": "1"})

    def test_parse_sections(self):
        text = "a = 1\n[db]\nhost = x\nport=5\n[other]\nk = v\n"
        self.assertEqual(
            parse(text),
            {"a": "1", "db.host": "x", "db.port": "5", "other.k": "v"},
        )

    def test_parse_no_equals_raises(self):
        with self.assertRaises(ValueError):
            parse("justakey\n")

    def test_parse_spaces(self):
        self.assertEqual(parse("  key  =  value  \n"), {"key": "value"})


class TestCfgMerge(unittest.TestCase):
    def test_merge_override_wins(self):
        self.assertEqual(merge({"a": "1"}, {"a": "2", "b": "3"}), {"a": "2", "b": "3"})

    def test_merge_empty_removes(self):
        self.assertEqual(merge({"a": "1", "b": "2"}, {"b": ""}), {"a": "1"})

    def test_merge_does_not_mutate(self):
        base = {"a": "1", "b": "2"}
        override = {"b": "", "c": "3"}
        result = merge(base, override)
        self.assertEqual(result, {"a": "1", "c": "3"})
        self.assertEqual(base, {"a": "1", "b": "2"})
        self.assertEqual(override, {"b": "", "c": "3"})
        self.assertIsNot(result, base)


class TestCfgCli(unittest.TestCase):
    def test_cli_merges_and_sorts(self):
        with tempfile.TemporaryDirectory() as d:
            base = os.path.join(d, "base.conf")
            over = os.path.join(d, "over.conf")
            with open(base, "w", encoding="utf-8") as f:
                f.write("a = 1\n[s]\nk = old\n")
            with open(over, "w", encoding="utf-8") as f:
                f.write("[s]\nk = new\nz = 9\n")
            out = io.StringIO()
            rc = main([base, over], out)
            self.assertEqual(rc, 0)
            self.assertEqual(out.getvalue(), "a=1\ns.k=new\ns.z=9\n")

    def test_cli_removal(self):
        with tempfile.TemporaryDirectory() as d:
            base = os.path.join(d, "base.conf")
            over = os.path.join(d, "over.conf")
            with open(base, "w", encoding="utf-8") as f:
                f.write("a = 1\nb = 2\n")
            with open(over, "w", encoding="utf-8") as f:
                f.write("b =\n")
            out = io.StringIO()
            rc = main([base, over], out)
            self.assertEqual(rc, 0)
            self.assertEqual(out.getvalue(), "a=1\n")


if __name__ == "__main__":
    unittest.main()
