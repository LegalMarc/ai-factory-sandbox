import io
import os
import tempfile
import unittest

from cfgcli import main
from cfgmerge import merge
from cfgparse import parse


class ParseTests(unittest.TestCase):
    def test_basic_key_value(self):
        self.assertEqual(parse("a = 1\nb=two\n"), {"a": "1", "b": "two"})

    def test_blank_and_comment_lines_are_skipped(self):
        self.assertEqual(parse("# comment\n\n  # indented\na = 1\n"), {"a": "1"})

    def test_sections_prefix_keys(self):
        self.assertEqual(
            parse("[db]\n host = x\nport=5\n"),
            {"db.host": "x", "db.port": "5"},
        )

    def test_key_without_equals_raises(self):
        with self.assertRaises(ValueError):
            parse("novalue\n")


class MergeTests(unittest.TestCase):
    def test_override_wins_and_inputs_unchanged(self):
        base = {"a": "1", "b": "2"}
        override = {"b": "3", "c": "4"}
        self.assertEqual(merge(base, override), {"a": "1", "b": "3", "c": "4"})
        self.assertEqual(base, {"a": "1", "b": "2"})
        self.assertEqual(override, {"b": "3", "c": "4"})

    def test_empty_value_removes_key(self):
        self.assertEqual(
            merge({"a": "1", "b": "2"}, {"b": "", "c": "3"}),
            {"a": "1", "c": "3"},
        )


class CliTests(unittest.TestCase):
    def test_main_prints_sorted_merged_config(self):
        with tempfile.TemporaryDirectory() as directory:
            base_path = os.path.join(directory, "base.conf")
            override_path = os.path.join(directory, "over.conf")
            with open(base_path, "w", encoding="utf-8") as handle:
                handle.write("a = 1\n[s]\nk = old\n")
            with open(override_path, "w", encoding="utf-8") as handle:
                handle.write("[s]\nk = new\nz = 9\n")
            stdout = io.StringIO()
            self.assertEqual(main([base_path, override_path], stdout), 0)
            self.assertEqual(stdout.getvalue(), "a=1\ns.k=new\ns.z=9\n")


if __name__ == "__main__":
    unittest.main()
