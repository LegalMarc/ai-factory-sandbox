import io
import os
import tempfile
import unittest

from cfgparse import parse
from cfgmerge import merge
from cfgcli import main


class TestParse(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(parse("a = 1\nb=2\n"), {"a": "1", "b": "2"})

    def test_comments_and_blank(self):
        self.assertEqual(parse("# c\n\n  # indented\na = 1\n"), {"a": "1"})

    def test_section(self):
        self.assertEqual(
            parse("a = 1\n[db]\nhost = x\nport=5\n"),
            {"a": "1", "db.host": "x", "db.port": "5"},
        )

    def test_missing_equals(self):
        with self.assertRaises(ValueError):
            parse("noequals\n")


class TestMerge(unittest.TestCase):
    def test_override_wins(self):
        self.assertEqual(merge({"a": "1"}, {"a": "2"}), {"a": "2"})

    def test_empty_removes(self):
        self.assertEqual(merge({"a": "1", "b": "2"}, {"b": ""}), {"a": "1"})

    def test_no_mutation(self):
        base = {"a": "1"}
        override = {"a": "2", "b": "3"}
        merge(base, override)
        self.assertEqual(base, {"a": "1"})
        self.assertEqual(override, {"a": "2", "b": "3"})


class TestCli(unittest.TestCase):
    def test_cli(self):
        with tempfile.TemporaryDirectory() as d:
            base_path = os.path.join(d, "base.conf")
            over_path = os.path.join(d, "over.conf")
            with open(base_path, "w", encoding="utf-8") as f:
                f.write("a = 1\n[s]\nk = old\n")
            with open(over_path, "w", encoding="utf-8") as f:
                f.write("[s]\nk = new\nz = 9\n")
            out = io.StringIO()
            result = main([base_path, over_path], out)
            self.assertEqual(result, 0)
            self.assertEqual(out.getvalue(), "a=1\ns.k=new\ns.z=9\n")


if __name__ == "__main__":
    unittest.main()
