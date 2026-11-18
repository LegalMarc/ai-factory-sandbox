import io
import os
import tempfile
import unittest

from cfgparse import parse
from cfgmerge import merge
import cfgcli


class ParseTests(unittest.TestCase):
    def test_basic_keys(self):
        self.assertEqual(parse("a = 1\n b=2 \n"), {"a": "1", "b": "2"})

    def test_blank_and_comments(self):
        self.assertEqual(parse("\n# comment\n  # another\na = 1\n"), {"a": "1"})

    def test_sections(self):
        text = "[db]\nhost = x\nport=5\n[web]\nport = 80\n"
        self.assertEqual(
            parse(text),
            {"db.host": "x", "db.port": "5", "web.port": "80"},
        )

    def test_missing_equals_raises(self):
        with self.assertRaises(ValueError):
            parse("broken line\n")

    def test_empty_value(self):
        self.assertEqual(parse("a =\n"), {"a": ""})


class MergeTests(unittest.TestCase):
    def test_override_wins(self):
        self.assertEqual(merge({"a": "1", "b": "2"}, {"b": "3"}), {"a": "1", "b": "3"})

    def test_empty_removes(self):
        self.assertEqual(merge({"a": "1", "b": "2"}, {"b": ""}), {"a": "1"})

    def test_does_not_mutate(self):
        base = {"a": "1"}
        override = {"b": "2"}
        merge(base, override)
        self.assertEqual(base, {"a": "1"})
        self.assertEqual(override, {"b": "2"})


class CliTests(unittest.TestCase):
    def test_main_prints_sorted_merged(self):
        directory = tempfile.mkdtemp()
        base_path = os.path.join(directory, "base.conf")
        over_path = os.path.join(directory, "over.conf")
        with open(base_path, "w") as handle:
            handle.write("a = 1\n[s]\nk = old\n")
        with open(over_path, "w") as handle:
            handle.write("[s]\nk = new\nz = 9\n")
        out = io.StringIO()
        self.assertEqual(cfgcli.main([base_path, over_path], out), 0)
        self.assertEqual(out.getvalue(), "a=1\ns.k=new\ns.z=9\n")


if __name__ == "__main__":
    unittest.main()
