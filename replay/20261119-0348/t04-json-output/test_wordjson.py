import io
import json
import unittest

from wordjson import main


class WordJsonTest(unittest.TestCase):
    def run_main(self, text, argv=()):
        stdin = io.StringIO(text)
        stdout = io.StringIO()
        result = main(list(argv), stdin, stdout)
        return result, stdout.getvalue()

    def test_plain_counts_and_orders(self):
        result, output = self.run_main("b a b\n")
        self.assertEqual(result, 0)
        self.assertEqual(output, "b 2\na 1\n")

    def test_json_document(self):
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
        self.assertEqual(
            output,
            '{\n'
            '  "total": 3,\n'
            '  "words": [\n'
            "    {\n"
            '      "word": "b",\n'
            '      "count": 2\n'
            "    },\n"
            "    {\n"
            '      "word": "a",\n'
            '      "count": 1\n'
            "    }\n"
            "  ]\n"
            "}\n",
        )

    def test_case_and_separators(self):
        result, output = self.run_main("Hello, WORLD! 42 hello...")
        self.assertEqual(result, 0)
        self.assertEqual(output, "hello 2\n42 1\nworld 1\n")

    def test_empty_plain(self):
        result, output = self.run_main("")
        self.assertEqual(result, 0)
        self.assertEqual(output, "")

    def test_empty_json(self):
        result, output = self.run_main("", ["--json"])
        self.assertEqual(result, 0)
        self.assertEqual(
            output,
            '{\n  "total": 0,\n  "words": []\n}\n',
        )


if __name__ == "__main__":
    unittest.main()
