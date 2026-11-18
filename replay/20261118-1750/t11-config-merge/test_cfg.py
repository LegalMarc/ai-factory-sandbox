import io
import os
import tempfile
import unittest

import cfgcli
import cfgmerge
import cfgparse


class ParseTests(unittest.TestCase):
    def test_basic_key_values(self):
        self.assertEqual(cfgparse.parse("a = 1\nb=two\n"), {"a": "1", "b": "two"})

    def test_sections(self):
        self.assertEqual(
            cfgparse.parse("[db]\n host = x\nport=5\n"), {"db.host": "x", "db.port": "5"}
        )

    def test_comments_and_blanks_skipped(self):
        self.assertEqual(cfgparse.parse("# c\n\n  # indented\na = 1\n"), {"a": "1"})

    def test_missing_equals_raises(self):
        with self.assertRaises(ValueError):
            cfgparse.parse("no equals here\n")


class MergeTests(unittest.TestCase):
    def test_override_wins(self):
        self.assertEqual(cfgmerge.merge({"a": "1"}, {"a": "2"}), {"a": "2"})

    def test_empty_string_removes(self):
        self.assertEqual(cfgmerge.merge({"a": "1", "b": "2"}, {"b": ""}), {"a": "1"})

    def test_arguments_unchanged(self):
        base = {"a": "1", "b": "2"}
        override = {"b": "", "c": "3"}
        cfgmerge.merge(base, override)
        self.assertEqual(base, {"a": "1", "b": "2"})
        self.assertEqual(override, {"b": "", "c": "3"})


class CliTests(unittest.TestCase):
    def test_main_prints_sorted_merged(self):
        d = tempfile.mkdtemp()
        base_path = os.path.join(d, "base.conf")
        over_path = os.path.join(d, "over.conf")
        with open(base_path, "w") as f:
            f.write("a = 1\n[s]\nk = old\n")
        with open(over_path, "w") as f:
            f.write("[s]\nk = new\nz = 9\n")
        out = io.StringIO()
        self.assertEqual(cfgcli.main([base_path, over_path], out), 0)
        self.assertEqual(out.getvalue(), "a=1\ns.k=new\ns.z=9\n")


if __name__ == "__main__":
    unittest.main()
