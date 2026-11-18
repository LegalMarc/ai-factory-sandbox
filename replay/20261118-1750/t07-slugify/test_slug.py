import unittest

from slug import slugify


class SlugifyTest(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_collapses_runs(self):
        self.assertEqual(slugify("a  b"), "a-b")
        self.assertEqual(slugify("a---b"), "a-b")

    def test_accents_removed(self):
        self.assertEqual(slugify("café über"), "cafe-uber")

    def test_no_leading_or_trailing_hyphen(self):
        self.assertEqual(slugify("  --Hello--  "), "hello")

    def test_only_allowed_characters(self):
        self.assertEqual(slugify("A1_b!c"), "a1-b-c")

    def test_empty(self):
        self.assertEqual(slugify(""), "")
        self.assertEqual(slugify("!!!"), "")


if __name__ == "__main__":
    unittest.main()
