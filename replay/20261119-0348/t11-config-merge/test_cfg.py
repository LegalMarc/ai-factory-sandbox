import io
import os
import tempfile
import unittest

from cfgparse import parse
from cfgmerge import merge
from cfgcli import main


class ParseTests(unittest.TestCase):
    def test_parse_simple(self):
        self.assertEqual(parse("a = 1\nb=2\n"), {"a": "1", "b": "2"})

    def test_parse_skips_blank_and_comments(self):
        self.assertEqual(parse("# c\n\n   # indented\n a = 1 \n"), {"a": "1"})

    def test_parse_sections(self):
        self.assertEqual(
            parse("[db]\nhost = x\nport=5\n"),
            {"db.host": "x", "db.port": "5"},
        )

    def test_parse_missing_equals_raises(self):
        with self.assertRaises(ValueError):
            parse("novalue\n")


class MergeTests(unittest.TestCase):
    def test_override_wins(self):
        self.assertEqual(merge({"a": "1", "b": "2"}, {"b": "3"}), {"a": "1", "b": "3"})

    def test_empty_removes_key(self):
        self.assertEqual(merge({"a": "1", "b": "2"}, {"b": ""}), {"a": "1"})

    def test_merge_does_not_mutate(self):
        base = {"a": "1"}
        override = {"a": "", "b": "2"}
        merge(base, override)
        self.assertEqual(base, {"a": "1"})
        self.assertEqual(override, {"a": "", "b": "2"})


class CliTests(unittest.TestCase):
    def test_main_merges_and_sorts(self):
        directory = tempfile.mkdtemp()
        base_path = os.path.join(directory, "base.conf")
        over_path = os.path.join(directory, "over.conf")
        with open(base_path, "w", encoding="utf-8") as handle:
            handle.write("a = 1\n[s]\nk = old\n")
        with open(over_path, "w", encoding="utf-8") as handle:
            handle.write("[s]\nk = new\nz = 9\n")
        out = io.StringIO()
        self.assertEqual(main([base_path, over_path], out), 0)
        self.assertEqual(out.getvalue(), "a=1\ns.k=new\ns.z=9\n")


if __name__ == "__main__":
    unittest.main()
