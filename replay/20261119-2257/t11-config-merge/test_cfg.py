import io
import os
import tempfile
import unittest

from cfgcli import main
from cfgmerge import merge
from cfgparse import parse


class TestParse(unittest.TestCase):
    def test_simple(self):
        self.assertEqual(parse("a = 1\nb=2\n"), {"a": "1", "b": "2"})

    def test_blank_and_comment(self):
        self.assertEqual(parse("# c\n\n  # hi\na = 1\n"), {"a": "1"})

    def test_section(self):
        text = "# c\na = 1\n\n[db]\n host = x\nport=5\n"
        self.assertEqual(parse(text), {"a": "1", "db.host": "x", "db.port": "5"})

    def test_missing_equals_raises(self):
        with self.assertRaises(ValueError):
            parse("nope\n")


class TestMerge(unittest.TestCase):
    def test_override_wins(self):
        self.assertEqual(merge({"a": "1"}, {"a": "2"}), {"a": "2"})

    def test_empty_removes(self):
        self.assertEqual(merge({"a": "1", "b": "2"}, {"b": "", "c": "3"}), {"a": "1", "c": "3"})

    def test_no_mutation(self):
        base = {"a": "1", "b": "2"}
        override = {"b": "", "c": "3"}
        result = merge(base, override)
        self.assertEqual(result, {"a": "1", "c": "3"})
        self.assertEqual(base, {"a": "1", "b": "2"})
        self.assertEqual(override, {"b": "", "c": "3"})


class TestCli(unittest.TestCase):
    def test_main_sorted(self):
        with tempfile.TemporaryDirectory() as d:
            base_path = os.path.join(d, "base.conf")
            over_path = os.path.join(d, "over.conf")
            with open(base_path, "w") as f:
                f.write("a = 1\n[s]\nk = old\n")
            with open(over_path, "w") as f:
                f.write("[s]\nk = new\nz = 9\n")
            out = io.StringIO()
            self.assertEqual(main([base_path, over_path], out), 0)
            self.assertEqual(out.getvalue(), "a=1\ns.k=new\ns.z=9\n")


if __name__ == "__main__":
    unittest.main()
