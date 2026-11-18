import unittest

from stack import Stack


class StackTest(unittest.TestCase):
    def test_new_stack_is_empty(self):
        stack = Stack()
        self.assertEqual(len(stack), 0)
        self.assertFalse(stack)

    def test_push_adds_items(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(len(stack), 2)
        self.assertTrue(stack)

    def test_pop_returns_newest_item(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)
        self.assertEqual(len(stack), 0)

    def test_peek_does_not_remove(self):
        stack = Stack()
        stack.push("a")
        stack.push("b")
        self.assertEqual(stack.peek(), "b")
        self.assertEqual(len(stack), 2)

    def test_pop_empty_raises_index_error(self):
        stack = Stack()
        self.assertRaises(IndexError, stack.pop)

    def test_peek_empty_raises_index_error(self):
        stack = Stack()
        self.assertRaises(IndexError, stack.peek)


if __name__ == "__main__":
    unittest.main()
