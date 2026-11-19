import unittest

from topwords import top_words


class TopWordsTests(unittest.TestCase):
    def test_most_frequent_first(self):
        self.assertEqual(top_words("b a b c a b", 2), [("b", 3), ("a", 2)])

    def test_ties_are_alphabetical(self):
        self.assertEqual(
            top_words("z y x", 3), [("x", 1), ("y", 1), ("z", 1)]
        )

    def test_stopwords_ignore_case(self):
        self.assertEqual(
            top_words("The cat the dog", 5, ("THE",)),
            [("cat", 1), ("dog", 1)],
        )

    def test_non_letter_characters_separate_words(self):
        self.assertEqual(
            top_words("Don't", 5), [("don", 1), ("t", 1)]
        )

    def test_non_positive_n_returns_empty_list(self):
        self.assertEqual(top_words("x y", 0), [])
        self.assertEqual(top_words("x y", -1), [])


if __name__ == "__main__":
    unittest.main()
