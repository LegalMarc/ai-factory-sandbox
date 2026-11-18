import unittest

from bounded import BoundedStack
from stack import Stack


class BoundedStackTest(unittest.TestCase):
    def test_is_a_stack(self):
        stack = BoundedStack(2)
        self.assertIsInstance(stack, Stack)
        self.assertEqual(len(stack), 0)

    def test_limit_below_one_raises_value_error(self):
        self.assertRaises(ValueError, BoundedStack, 0)
        self.assertRaises(ValueError, BoundedStack, -1)

    def test_push_up_to_limit(self):
        stack = BoundedStack(2)
        stack.push(1)
        stack.push(2)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 2)

    def test_push_beyond_limit_raises_and_leaves_stack_unchanged(self):
        stack = BoundedStack(2)
        stack.push(1)
        stack.push(2)
        self.assertRaises(OverflowError, stack.push, 3)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 2)

    def test_pop_then_push_again(self):
        stack = BoundedStack(2)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        stack.push(9)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 9)

    def test_peek_and_pop_empty_raise_index_error(self):
        stack = BoundedStack(1)
        self.assertRaises(IndexError, stack.peek)
        self.assertRaises(IndexError, stack.pop)


if __name__ == "__main__":
    unittest.main()
