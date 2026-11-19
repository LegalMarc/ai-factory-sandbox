import unittest

from moneyfmt import round_half_up


class TestRoundHalfUp(unittest.TestCase):
    def test_basic_rounding(self):
        self.assertEqual(round_half_up("3.14159", 2), "3.14")
        self.assertEqual(round_half_up("10", 2), "10.00")
        self.assertEqual(round_half_up("7.9", 0), "8")
        self.assertEqual(round_half_up("-1.234", 1), "-1.2")

    def test_money_case_exact_decimal(self):
        self.assertEqual(round_half_up("2.675", 2), "2.68")
        self.assertEqual(round_half_up("1.005", 2), "1.01")

    def test_half_away_from_zero(self):
        self.assertEqual(round_half_up("0.5", 0), "1")
        self.assertEqual(round_half_up("-0.5", 0), "-1")
        self.assertEqual(round_half_up("2.5", 0), "3")
        self.assertEqual(round_half_up("-2.5", 0), "-3")

    def test_trailing_zeros_and_format(self):
        self.assertEqual(round_half_up("1.2", 3), "1.200")
        self.assertEqual(round_half_up("0", 0), "0")
        self.assertEqual(round_half_up("9.995", 2), "10.00")
        self.assertEqual(round_half_up("-0.004", 2), "0.00")
        self.assertEqual(round_half_up("1e20", 0), "100000000000000000000")

    def test_invalid_raises_value_error(self):
        for bad in ["", "abc", "1.2.3", "NaN", "inf", "-inf", "1,000", "--1"]:
            with self.subTest(bad=bad):
                with self.assertRaises(ValueError):
                    round_half_up(bad, 2)
        with self.assertRaises(ValueError):
            round_half_up("1.5", -1)


if __name__ == "__main__":
    unittest.main()
