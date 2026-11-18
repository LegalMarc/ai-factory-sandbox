import io
import json
import unittest

from wordjson import main


def run(text, *args):
    stdout = io.StringIO()
    result = main(list(args), io.StringIO(text), stdout)
    return result, stdout.getvalue()


class WordJsonTest(unittest.TestCase):
    def test_plain_counts_and_order(self):
        result, output = run("b a b\n")
        self.assertEqual(result, 0)
        self.assertEqual(output, "b 2\na 1\n")

    def test_json_output(self):
        result, output = run("b a b\n", "--json")
        self.assertEqual(result, 0)
        self.assertTrue(output.endswith("}\n"))
        self.assertFalse(output.endswith("\n\n"))
        self.assertEqual(
            json.loads(output),
            {
                "total": 3,
                "words": [
                    {"word": "b", "count": 2},
                    {"word": "a", "count": 1},
                ],
            },
        )

    def test_empty_input(self):
        result, output = run("")
        self.assertEqual(result, 0)
        self.assertEqual(output, "")
        result, output = run("", "--json")
        self.assertEqual(result, 0)
        self.assertEqual(json.loads(output), {"total": 0, "words": []})

    def test_word_splitting_and_case(self):
        result, output = run("Hello, WORLD! hello 42-42\n")
        self.assertEqual(result, 0)
        self.assertEqual(output, "42 2\nhello 2\nworld 1\n")


if __name__ == "__main__":
    unittest.main()
