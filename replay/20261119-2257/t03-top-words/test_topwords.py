import unittest

from topwords import top_words


class TestTopWords(unittest.TestCase):
    def test_most_frequent(self):
        self.assertEqual(top_words("b a b c a b", 2), [("b", 3), ("a", 2)])

    def test_alphabetical_tiebreak(self):
        self.assertEqual(top_words("z y x", 5), [("x", 1), ("y", 1), ("z", 1)])

    def test_stopwords_case_insensitive(self):
        self.assertEqual(
            top_words("The cat the dog", 5, ("THE",)), [("cat", 1), ("dog", 1)]
        )

    def test_n_zero(self):
        self.assertEqual(top_words("x y", 0), [])

    def test_apostrophe_splits(self):
        self.assertEqual(top_words("Don't", 5), [("don", 1), ("t", 1)])

    def test_default_n_and_digits(self):
        self.assertEqual(
            top_words("a1 a1 a1 b b c"),
            [("a1", 3), ("b", 2), ("c", 1)],
        )


if __name__ == "__main__":
    unittest.main()
