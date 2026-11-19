import unittest

from slug import slugify


class SlugifyTests(unittest.TestCase):
    def test_basic_title(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_collapses_runs(self):
        self.assertEqual(slugify("a  b"), "a-b")
        self.assertEqual(slugify("a---b"), "a-b")

    def test_removes_accents(self):
        self.assertEqual(slugify("Café Über"), "cafe-uber")

    def test_no_leading_or_trailing_dash(self):
        self.assertEqual(slugify("  --Hello--  "), "hello")

    def test_empty_and_symbols(self):
        self.assertEqual(slugify(""), "")
        self.assertEqual(slugify("!!! ???"), "")

    def test_keeps_digits(self):
        self.assertEqual(slugify("Top 10 Songs"), "top-10-songs")


if __name__ == "__main__":
    unittest.main()
