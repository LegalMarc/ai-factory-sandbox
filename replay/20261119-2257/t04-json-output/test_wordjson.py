import io
import json
import unittest

from wordjson import main


def run(argv, text):
    stdin = io.StringIO(text)
    stdout = io.StringIO()
    result = main(argv, stdin, stdout)
    return result, stdout.getvalue()


class TestWordJson(unittest.TestCase):
    def test_plain_ordering(self):
        result, out = run([], "b a b\n")
        self.assertEqual(result, 0)
        self.assertEqual(out, "b 2\na 1\n")

    def test_json_output(self):
        result, out = run(["--json"], "b a b\n")
        self.assertEqual(result, 0)
        self.assertTrue(out.endswith("}\n"))
        self.assertFalse(out.endswith("\n\n"))
        self.assertEqual(
            json.loads(out),
            {"total": 3, "words": [{"word": "b", "count": 2}, {"word": "a", "count": 1}]},
        )
        self.assertEqual(out.splitlines()[1], '  "total": 3,')

    def test_empty_input(self):
        result, out = run([], "")
        self.assertEqual(result, 0)
        self.assertEqual(out, "")
        result, out = run(["--json"], "")
        self.assertEqual(result, 0)
        self.assertEqual(json.loads(out), {"total": 0, "words": []})
        self.assertEqual(out, '{\n  "total": 0,\n  "words": []\n}\n')

    def test_tie_alphabetical_and_case(self):
        result, out = run([], "Dog cat DOG bird cat dog!\n")
        self.assertEqual(result, 0)
        self.assertEqual(out, "dog 3\ncat 2\nbird 1\n")


if __name__ == "__main__":
    unittest.main()
