import unittest

from moneyfmt import round_half_up


class RoundHalfUpTests(unittest.TestCase):
    def test_rounds_to_requested_places(self):
        self.assertEqual(round_half_up("3.14159", 2), "3.14")
        self.assertEqual(round_half_up("-1.234", 1), "-1.2")

    def test_pads_with_trailing_zeros(self):
        self.assertEqual(round_half_up("10", 2), "10.00")
        self.assertEqual(round_half_up("7.9", 0), "8")
        self.assertEqual(round_half_up("0.1", 2), "0.10")

    def test_halves_round_away_from_zero(self):
        self.assertEqual(round_half_up("0.5", 0), "1")
        self.assertEqual(round_half_up("-0.5", 0), "-1")
        self.assertEqual(round_half_up("2.675", 2), "2.68")
        self.assertEqual(round_half_up("-2.675", 2), "-2.68")

    def test_uses_exact_decimal_not_binary_float(self):
        self.assertEqual(round_half_up("1.005", 2), "1.01")

    def test_negative_values(self):
        self.assertEqual(round_half_up("-2.5", 0), "-3")
        self.assertEqual(round_half_up("-0.004", 2), "0.00")

    def test_non_numeric_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            round_half_up("not a number", 2)
        with self.assertRaises(ValueError):
            round_half_up("", 0)

    def test_invalid_places_raises_value_error(self):
        with self.assertRaises(ValueError):
            round_half_up("1.23", -1)


if __name__ == "__main__":
    unittest.main()
