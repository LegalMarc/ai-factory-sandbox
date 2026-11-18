import unittest

from moneyfmt import round_half_up


class RoundHalfUpTests(unittest.TestCase):
    def test_rounds_to_requested_places(self):
        self.assertEqual(round_half_up("3.14159", 2), "3.14")
        self.assertEqual(round_half_up("-1.234", 1), "-1.2")

    def test_pads_with_trailing_zeros(self):
        self.assertEqual(round_half_up("10", 2), "10.00")
        self.assertEqual(round_half_up("7.9", 0), "8")

    def test_halves_round_away_from_zero(self):
        self.assertEqual(round_half_up("2.675", 2), "2.68")
        self.assertEqual(round_half_up("0.5", 0), "1")
        self.assertEqual(round_half_up("-0.5", 0), "-1")

    def test_uses_exact_decimal_not_binary_float(self):
        self.assertEqual(round_half_up("1.005", 2), "1.01")
        self.assertEqual(round_half_up("0.1", 2), "0.10")

    def test_negative_result_that_rounds_to_zero_is_not_negative(self):
        self.assertEqual(round_half_up("-0.4", 0), "0")

    def test_non_numeric_value_raises_value_error(self):
        for bad in ("abc", "", "1.2.3", "NaN", "Infinity"):
            with self.assertRaises(ValueError):
                round_half_up(bad, 2)


if __name__ == "__main__":
    unittest.main()
