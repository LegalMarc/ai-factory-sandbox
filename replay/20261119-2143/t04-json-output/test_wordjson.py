import io
import json
import unittest

from wordjson import main


def run(argv, inp):
    out = io.StringIO()
    rc = main(argv, io.StringIO(inp), out)
    return rc, out.getvalue()


class TestWordjson(unittest.TestCase):
    def test_plain(self):
        rc, out = run(["wordjson.py"], "b a b\n")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "b 2\na 1\n")

    def test_json(self):
        rc, out = run(["wordjson.py", "--json"], "b a b\n")
        self.assertEqual(rc, 0)
        self.assertTrue(out.endswith("\n") and not out.endswith("\n\n"))
        self.assertEqual(
            json.loads(out),
            {"total": 3, "words": [{"word": "b", "count": 2}, {"word": "a", "count": 1}]},
        )
        self.assertEqual(out.splitlines()[1], '  "total": 3,')

    def test_empty_json(self):
        rc, out = run(["wordjson.py", "--json"], "")
        self.assertEqual(rc, 0)
        self.assertEqual(json.loads(out), {"total": 0, "words": []})

    def test_empty_plain_and_ordering(self):
        rc, out = run(["wordjson.py"], "")
        self.assertEqual(out, "")
        rc, out = run(["wordjson.py"], "B!a B2 a2 b2")
        self.assertEqual(rc, 0)
        self.assertEqual(out, "b2 2\na 1\na2 1\nb 1\n")


if __name__ == "__main__":
    unittest.main()
