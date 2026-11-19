import unittest

from bounded import BoundedStack
from stack import Stack


class TestBoundedStack(unittest.TestCase):
    def test_is_subclass_and_inherits_behaviour(self):
        s = BoundedStack(2)
        self.assertIsInstance(s, Stack)
        s.push(1)
        s.push(2)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertFalse(s)

    def test_invalid_limit_raises_value_error(self):
        with self.assertRaises(ValueError):
            BoundedStack(0)
        with self.assertRaises(ValueError):
            BoundedStack(-1)

    def test_push_over_limit_raises_and_unchanged(self):
        s = BoundedStack(2)
        s.push(1)
        s.push(2)
        with self.assertRaises(OverflowError):
            s.push(3)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_push_after_pop_works(self):
        s = BoundedStack(2)
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        s.push(9)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.peek(), 9)

    def test_inherited_empty_behaviour(self):
        s = BoundedStack(1)
        with self.assertRaises(IndexError):
            s.pop()
        with self.assertRaises(IndexError):
            s.peek()


if __name__ == "__main__":
    unittest.main()
