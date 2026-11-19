import unittest

from moneyfmt import round_half_up


class TestRoundHalfUp(unittest.TestCase):
    def test_money_example(self):
        self.assertEqual(round_half_up("2.675", 2), "2.68")

    def test_basic_rounding(self):
        self.assertEqual(round_half_up("3.14159", 2), "3.14")
        self.assertEqual(round_half_up("-1.234", 1), "-1.2")
        self.assertEqual(round_half_up("7.9", 0), "8")

    def test_half_away_from_zero(self):
        self.assertEqual(round_half_up("0.5", 0), "1")
        self.assertEqual(round_half_up("-0.5", 0), "-1")
        self.assertEqual(round_half_up("2.5", 0), "3")
        self.assertEqual(round_half_up("-2.5", 0), "-3")
        self.assertEqual(round_half_up("1.005", 2), "1.01")
        self.assertEqual(round_half_up("-1.005", 2), "-1.01")

    def test_exact_places_formatting(self):
        self.assertEqual(round_half_up("10", 2), "10.00")
        self.assertEqual(round_half_up("10", 0), "10")
        self.assertEqual(round_half_up("1.2", 3), "1.200")
        self.assertEqual(round_half_up("0", 2), "0.00")

    def test_invalid_value(self):
        with self.assertRaises(ValueError):
            round_half_up("not-a-number", 2)
        with self.assertRaises(ValueError):
            round_half_up("", 2)


if __name__ == "__main__":
    unittest.main()
