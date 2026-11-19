import unittest

from bounded import BoundedStack
from stack import Stack


class TestBoundedStack(unittest.TestCase):
    def test_invalid_limit(self):
        with self.assertRaises(ValueError):
            BoundedStack(0)
        with self.assertRaises(ValueError):
            BoundedStack(-1)

    def test_push_until_limit_then_overflow(self):
        s = BoundedStack(2)
        self.assertIsInstance(s, Stack)
        s.push(1)
        s.push(2)
        with self.assertRaises(OverflowError):
            s.push(3)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.peek(), 2)

    def test_pop_frees_space_and_lifo(self):
        s = BoundedStack(2)
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        s.push(9)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.peek(), 9)
        self.assertEqual(s.pop(), 9)
        self.assertEqual(s.pop(), 1)


if __name__ == "__main__":
    unittest.main()
