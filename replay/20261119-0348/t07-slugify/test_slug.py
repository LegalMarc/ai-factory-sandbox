import unittest

from slug import slugify


class SlugifyTests(unittest.TestCase):
    def test_basic_phrase(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_runs_of_other_characters_collapse(self):
        self.assertEqual(slugify("a  b---c__d"), "a-b-c-d")

    def test_accents_are_removed(self):
        self.assertEqual(slugify("Café Über"), "cafe-uber")

    def test_no_leading_or_trailing_hyphens(self):
        self.assertEqual(slugify("  --Hello!!  "), "hello")

    def test_no_letters_or_digits(self):
        self.assertEqual(slugify("!!!"), "")
        self.assertEqual(slugify(""), "")


if __name__ == "__main__":
    unittest.main()
