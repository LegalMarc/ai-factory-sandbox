import unittest

from bounded import BoundedStack
from stack import Stack


class BoundedStackTest(unittest.TestCase):
    def test_is_a_stack(self):
        stack = BoundedStack(2)
        self.assertIsInstance(stack, Stack)
        self.assertEqual(len(stack), 0)

    def test_rejects_limit_below_one(self):
        with self.assertRaises(ValueError):
            BoundedStack(0)
        with self.assertRaises(ValueError):
            BoundedStack(-1)

    def test_push_up_to_limit(self):
        stack = BoundedStack(2)
        stack.push(1)
        stack.push(2)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 2)

    def test_push_past_limit_raises_and_leaves_stack_unchanged(self):
        stack = BoundedStack(2)
        stack.push(1)
        stack.push(2)
        with self.assertRaises(OverflowError):
            stack.push(3)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 2)
        self.assertEqual(stack.pop(), 2)
        stack.push(9)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 9)

    def test_inherited_behaviour(self):
        stack = BoundedStack(3)
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()
        stack.push("a")
        self.assertTrue(stack)
        self.assertEqual(stack.pop(), "a")
        self.assertFalse(stack)


if __name__ == "__main__":
    unittest.main()
