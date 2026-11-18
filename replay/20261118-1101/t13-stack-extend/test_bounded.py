import unittest

from bounded import BoundedStack
from stack import Stack


class TestBoundedStack(unittest.TestCase):
    def test_is_a_stack(self):
        self.assertIsInstance(BoundedStack(1), Stack)

    def test_rejects_limit_below_one(self):
        with self.assertRaises(ValueError):
            BoundedStack(0)
        with self.assertRaises(ValueError):
            BoundedStack(-3)

    def test_push_within_limit(self):
        stack = BoundedStack(2)
        stack.push(1)
        stack.push(2)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 2)

    def test_push_beyond_limit_raises_and_leaves_stack_unchanged(self):
        stack = BoundedStack(2)
        stack.push(1)
        stack.push(2)
        with self.assertRaises(OverflowError):
            stack.push(3)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 2)

    def test_pop_frees_room_to_push(self):
        stack = BoundedStack(2)
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        stack.push(9)
        self.assertEqual(len(stack), 2)
        self.assertEqual(stack.peek(), 9)

    def test_empty_pop_and_peek_behave_like_stack(self):
        stack = BoundedStack(3)
        with self.assertRaises(IndexError):
            stack.pop()
        with self.assertRaises(IndexError):
            stack.peek()


if __name__ == "__main__":
    unittest.main()
