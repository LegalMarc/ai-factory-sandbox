import unittest

from moneyfmt import round_half_up


class RoundHalfUpTests(unittest.TestCase):
    def test_rounds_away_from_zero_on_half(self):
        self.assertEqual(round_half_up("0.5", 0), "1")
        self.assertEqual(round_half_up("-0.5", 0), "-1")

    def test_money_case_is_exact(self):
        self.assertEqual(round_half_up("2.675", 2), "2.68")

    def test_fills_requested_places(self):
        self.assertEqual(round_half_up("10", 2), "10.00")
        self.assertEqual(round_half_up("3.14159", 2), "3.14")
        self.assertEqual(round_half_up("7.9", 0), "8")

    def test_negative_values(self):
        self.assertEqual(round_half_up("-1.234", 1), "-1.2")
        self.assertEqual(round_half_up("-2.5", 0), "-3")

    def test_invalid_value_raises_value_error(self):
        with self.assertRaises(ValueError):
            round_half_up("not a number", 2)

    def test_invalid_places_raises_value_error(self):
        with self.assertRaises(ValueError):
            round_half_up("1.23", -1)


if __name__ == "__main__":
    unittest.main()
