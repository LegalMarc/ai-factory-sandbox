import unittest

from bounded import BoundedStack
from stack import Stack


class TestBoundedStack(unittest.TestCase):
    def test_is_stack_subclass(self):
        s = BoundedStack(2)
        self.assertIsInstance(s, Stack)

    def test_invalid_limit(self):
        with self.assertRaises(ValueError):
            BoundedStack(0)
        with self.assertRaises(ValueError):
            BoundedStack(-1)

    def test_push_overflow(self):
        s = BoundedStack(2)
        s.push(1)
        s.push(2)
        with self.assertRaises(OverflowError):
            s.push(3)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.peek(), 2)

    def test_push_after_pop(self):
        s = BoundedStack(2)
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        s.push(9)
        self.assertEqual(len(s), 2)
        self.assertEqual(s.peek(), 9)

    def test_inherited_behaviour(self):
        s = BoundedStack(3)
        with self.assertRaises(IndexError):
            s.pop()
        with self.assertRaises(IndexError):
            s.peek()
        self.assertFalse(s)
        s.push("a")
        self.assertTrue(s)


if __name__ == "__main__":
    unittest.main()
