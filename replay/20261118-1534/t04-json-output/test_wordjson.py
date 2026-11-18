import io
import json
import unittest

import wordjson


class WordJsonTest(unittest.TestCase):
    def run_main(self, text, *args):
        stdout = io.StringIO()
        result = wordjson.main(list(args), io.StringIO(text), stdout)
        return result, stdout.getvalue()

    def test_plain_output(self):
        result, output = self.run_main("b a b\n")
        self.assertEqual(result, 0)
        self.assertEqual(output, "b 2\na 1\n")

    def test_json_output(self):
        result, output = self.run_main("b a b\n", "--json")
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
        result, output = self.run_main("")
        self.assertEqual(result, 0)
        self.assertEqual(output, "")

    def test_empty_json_output(self):
        result, output = self.run_main("", "--json")
        self.assertEqual(result, 0)
        self.assertEqual(output, '{\n  "total": 0,\n  "words": []\n}\n')

    def test_counts_and_order(self):
        result, output = self.run_main("Hello, hello! WORLD 42 world 42 42")
        self.assertEqual(result, 0)
        self.assertEqual(output, "42 3\nhello 2\nworld 2\n")


if __name__ == "__main__":
    unittest.main()
