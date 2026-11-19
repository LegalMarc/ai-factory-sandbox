import io
import os
import tempfile
import unittest

from cfgparse import parse
from cfgmerge import merge
from cfgcli import main


class TestCfgParse(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(parse("a = 1\nb=2\n"), {"a": "1", "b": "2"})

    def test_comments_and_blank(self):
        self.assertEqual(parse("# c\n\n  # indented\na = 1\n"), {"a": "1"})

    def test_section(self):
        self.assertEqual(
            parse("[db]\nhost = x\nport=5\n"),
            {"db.host": "x", "db.port": "5"},
        )

    def test_no_equals_raises(self):
        with self.assertRaises(ValueError):
            parse("badline\n")


class TestCfgMerge(unittest.TestCase):
    def test_override_wins(self):
        self.assertEqual(merge({"a": "1"}, {"a": "2"}), {"a": "2"})

    def test_empty_removes(self):
        self.assertEqual(merge({"a": "1", "b": "2"}, {"b": ""}), {"a": "1"})

    def test_no_mutation(self):
        base = {"a": "1", "b": "2"}
        override = {"b": "", "c": "3"}
        result = merge(base, override)
        self.assertEqual(result, {"a": "1", "c": "3"})
        self.assertEqual(base, {"a": "1", "b": "2"})
        self.assertEqual(override, {"b": "", "c": "3"})


class TestCfgCli(unittest.TestCase):
    def test_main_sorted(self):
        with tempfile.TemporaryDirectory() as d:
            base = os.path.join(d, "base.conf")
            over = os.path.join(d, "over.conf")
            with open(base, "w") as f:
                f.write("a = 1\n[s]\nk = old\n")
            with open(over, "w") as f:
                f.write("[s]\nk = new\nz = 9\n")
            out = io.StringIO()
            rc = main([base, over], out)
            self.assertEqual(rc, 0)
            self.assertEqual(out.getvalue(), "a=1\ns.k=new\ns.z=9\n")

    def test_main_removal(self):
        with tempfile.TemporaryDirectory() as d:
            base = os.path.join(d, "base.conf")
            over = os.path.join(d, "over.conf")
            with open(base, "w") as f:
                f.write("a = 1\nb = 2\n")
            with open(over, "w") as f:
                f.write("b =\n")
            out = io.StringIO()
            rc = main([base, over], out)
            self.assertEqual(rc, 0)
            self.assertEqual(out.getvalue(), "a=1\n")


if __name__ == "__main__":
    unittest.main()
