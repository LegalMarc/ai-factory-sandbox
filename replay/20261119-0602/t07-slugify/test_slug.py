import unittest

from slug import slugify


class SlugifyTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_collapses_runs(self):
        self.assertEqual(slugify("a  b"), "a-b")
        self.assertEqual(slugify("a---b___c"), "a-b-c")

    def test_accents_removed(self):
        self.assertEqual(slugify("Café Über"), "cafe-uber")

    def test_no_leading_or_trailing_dash(self):
        self.assertEqual(slugify("--hello--"), "hello")
        self.assertEqual(slugify("!?! hello !?!"), "hello")

    def test_no_letters_or_digits(self):
        self.assertEqual(slugify(""), "")
        self.assertEqual(slugify("!@#$%^&*()"), "")

    def test_only_allowed_characters(self):
        result = slugify("Some Title: Part 2 (Revised)")
        self.assertRegex(result, r"^[a-z0-9-]*$")


if __name__ == "__main__":
    unittest.main()
