import io
import json
import unittest

from wordjson import main


class TestWordJson(unittest.TestCase):
    def run_main(self, args, text):
        stdout = io.StringIO()
        result = main(args, io.StringIO(text), stdout)
        self.assertEqual(result, 0)
        return stdout.getvalue()

    def test_plain_output(self):
        self.assertEqual(
            self.run_main([], "b a b\n"), "b 2\na 1\n"
        )

    def test_json_output(self):
        output = self.run_main(["--json"], "b a b\n")
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
        self.assertTrue(output.endswith("}\n"))
        self.assertFalse(output.endswith("\n\n"))

    def test_empty_input(self):
        self.assertEqual(self.run_main([], ""), "")
        output = self.run_main(["--json"], "")
        self.assertEqual(
            json.loads(output), {"total": 0, "words": []}
        )

    def test_ordering_and_separators(self):
        output = self.run_main([], "B, b! A a_c 123 123\n")
        self.assertEqual(
            output, "123 2\na 2\nb 2\nc 1\n"
        )


if __name__ == "__main__":
    unittest.main()
