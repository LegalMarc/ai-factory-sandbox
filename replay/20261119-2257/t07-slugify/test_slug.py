import unittest

from slug import slugify


class TestSlugify(unittest.TestCase):
    def test_hello_world(self):
        self.assertEqual(slugify("Hello, World!"), "hello-world")

    def test_runs_become_single_dash(self):
        self.assertEqual(slugify("a  b"), "a-b")
        self.assertEqual(slugify("a---b___c"), "a-b-c")

    def test_accents_stripped(self):
        self.assertEqual(slugify("café"), "cafe")
        self.assertEqual(slugify("über"), "uber")
        self.assertEqual(slugify("Crème Brûlée"), "creme-brulee")

    def test_non_ascii_separators_become_dash(self):
        self.assertEqual(slugify("Hello—World"), "hello-world")
        self.assertEqual(slugify("a€b"), "a-b")
        self.assertEqual(slugify("aøb"), "a-b")

    def test_no_leading_trailing_dash(self):
        self.assertEqual(slugify("--Hello--"), "hello")
        self.assertEqual(slugify("  hi  "), "hi")

    def test_no_alphanumeric_gives_empty(self):
        self.assertEqual(slugify(""), "")
        self.assertEqual(slugify("!!! --- ???"), "")

    def test_only_allowed_characters(self):
        result = slugify("Hello, World! 123 #@é")
        self.assertEqual(result, "hello-world-123-e")
        self.assertTrue(all(c.islower() or c.isdigit() or c == "-" for c in result))


if __name__ == "__main__":
    unittest.main()
