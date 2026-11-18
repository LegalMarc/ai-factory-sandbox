import unittest

from slug import slugify


class SlugifyTests(unittest.TestCase):
    def test_basic(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_only_allowed_characters(self):
        result = slugify("Foo_bar!! baz---qux")
        self.assertTrue(all(c.isdigit() or "a" <= c <= "z" or c == "-" for c in result))

    def test_accents_removed(self):
        self.assertEqual(slugify("café über"), "cafe-uber")

    def test_no_leading_or_trailing_hyphen(self):
        self.assertEqual(slugify("  --Hello--  "), "hello")

    def test_no_letters_or_digits(self):
        self.assertEqual(slugify("!!!"), "")
        self.assertEqual(slugify(""), "")

    def test_runs_collapse_to_single_hyphen(self):
        self.assertEqual(slugify("a  b"), "a-b")


if __name__ == "__main__":
    unittest.main()
