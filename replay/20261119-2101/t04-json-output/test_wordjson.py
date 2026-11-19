import io
import json
import unittest

import wordjson


class WordJsonTests(unittest.TestCase):
    def run_main(self, text, argv=None):
        stdout = io.StringIO()
        result = wordjson.main(argv or [], io.StringIO(text), stdout)
        return result, stdout.getvalue()

    def test_plain_output_ordering(self):
        result, output = self.run_main("b a b\n")
        self.assertEqual(result, 0)
        self.assertEqual(output, "b 2\na 1\n")

    def test_ties_are_alphabetical_and_separators(self):
        _, output = self.run_main("Zebra apple, apple! zebra? 42 42")
        self.assertEqual(output, "42 2\napple 2\nzebra 2\n")

    def test_json_output(self):
        result, output = self.run_main("b a b\n", ["--json"])
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
        _, output = self.run_main("")
        self.assertEqual(output, "")
        _, json_output = self.run_main("", ["--json"])
        self.assertEqual(json.loads(json_output), {"total": 0, "words": []})


if __name__ == "__main__":
    unittest.main()
