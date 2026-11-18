import unittest

from bounded import BoundedStack
from stack import Stack


class BoundedStackTest(unittest.TestCase):
    def test_is_a_stack(self):
        self.assertIsInstance(BoundedStack(2), Stack)

    def test_invalid_limit_raises_value_error(self):
        self.assertRaises(ValueError, BoundedStack, 0)
        self.assertRaises(ValueError, BoundedStack, -1)

    def test_push_within_limit(self):
        stack = BoundedStack(2)
        stack.push(1)
        stack.push(2)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 2)

    def test_push_past_limit_raises_and_leaves_stack_unchanged(self):
        stack = BoundedStack(2)
        stack.push(1)
        stack.push(2)
        self.assertRaises(OverflowError, stack.push, 3)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 2)

    def test_push_after_pop(self):
        stack = BoundedStack(2)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        stack.push(9)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 9)

    def test_pop_empty_raises_index_error(self):
        stack = BoundedStack(3)
        self.assertRaises(IndexError, stack.pop)


if __name__ == "__main__":
    unittest.main()
