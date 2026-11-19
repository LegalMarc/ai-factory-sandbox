import io
import os
import tempfile
import unittest

from cfgparse import parse
from cfgmerge import merge
from cfgcli import main


class TestParse(unittest.TestCase):
    def test_simple_key_value(self):
        self.assertEqual(parse("a = 1\nb = 2\n"), {"a": "1", "b": "2"})

    def test_spaces_trimmed(self):
        self.assertEqual(parse("  a   =   1  \n"), {"a": "1"})

    def test_comments_and_blanks_skipped(self):
        self.assertEqual(parse("# c\n\n  # indented\na = 1\n\n"), {"a": "1"})

    def test_section_prefix(self):
        text = "a = 1\n[db]\nhost = x\nport = 5\n"
        self.assertEqual(parse(text), {"a": "1", "db.host": "x", "db.port": "5"})

    def test_section_switch(self):
        text = "[s1]\nk = 1\n[s2]\nk = 2\n"
        self.assertEqual(parse(text), {"s1.k": "1", "s2.k": "2"})

    def test_missing_equals_raises(self):
        with self.assertRaises(ValueError):
            parse("noequals\n")


class TestMerge(unittest.TestCase):
    def test_override_wins(self):
        self.assertEqual(merge({"a": "1"}, {"a": "2"}), {"a": "2"})

    def test_empty_string_deletes(self):
        self.assertEqual(merge({"a": "1", "b": "2"}, {"b": ""}), {"a": "1"})

    def test_does_not_mutate_inputs(self):
        base = {"a": "1", "b": "2"}
        override = {"b": "", "c": "3"}
        result = merge(base, override)
        self.assertEqual(result, {"a": "1", "c": "3"})
        self.assertEqual(base, {"a": "1", "b": "2"})
        self.assertEqual(override, {"b": "", "c": "3"})


class TestCli(unittest.TestCase):
    def test_main_merges_and_sorts(self):
        with tempfile.TemporaryDirectory() as d:
            base_path = os.path.join(d, "base.conf")
            over_path = os.path.join(d, "over.conf")
            with open(base_path, "w") as f:
                f.write("a = 1\n[s]\nk = old\n")
            with open(over_path, "w") as f:
                f.write("[s]\nk = new\nz = 9\n")
            out = io.StringIO()
            rc = main([base_path, over_path], out)
            self.assertEqual(rc, 0)
            self.assertEqual(out.getvalue(), "a=1\ns.k=new\ns.z=9\n")

    def test_main_deletion(self):
        with tempfile.TemporaryDirectory() as d:
            base_path = os.path.join(d, "base.conf")
            over_path = os.path.join(d, "over.conf")
            with open(base_path, "w") as f:
                f.write("a = 1\nb = 2\n")
            with open(over_path, "w") as f:
                f.write("b =\n")
            out = io.StringIO()
            rc = main([base_path, over_path], out)
            self.assertEqual(rc, 0)
            self.assertEqual(out.getvalue(), "a=1\n")


if __name__ == "__main__":
    unittest.main()
