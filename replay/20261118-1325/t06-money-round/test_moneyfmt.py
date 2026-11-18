import unittest

from moneyfmt import round_half_up


class RoundHalfUpTests(unittest.TestCase):
    def test_rounds_to_places(self):
        self.assertEqual(round_half_up("3.14159", 2), "3.14")
        self.assertEqual(round_half_up("-1.234", 1), "-1.2")

    def test_pads_to_exact_places(self):
        self.assertEqual(round_half_up("10", 2), "10.00")
        self.assertEqual(round_half_up("7.9", 0), "8")

    def test_halves_round_away_from_zero(self):
        self.assertEqual(round_half_up("2.675", 2), "2.68")
        self.assertEqual(round_half_up("0.5", 0), "1")
        self.assertEqual(round_half_up("-0.5", 0), "-1")

    def test_rejects_non_numbers(self):
        for bad in ("abc", "", "1.2.3", "NaN", "Infinity"):
            with self.assertRaises(ValueError):
                round_half_up(bad, 2)

    def test_negative_result_that_rounds_to_zero_is_not_negative(self):
        self.assertEqual(round_half_up("-0.4", 0), "0")


if __name__ == "__main__":
    unittest.main()
