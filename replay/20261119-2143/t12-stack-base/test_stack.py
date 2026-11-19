import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    def test_empty_len_and_bool(self):
        s = Stack()
        self.assertEqual(len(s), 0)
        self.assertFalse(s)

    def test_pop_empty_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_peek_empty_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.peek()

    def test_push_peek_pop_lifo(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.peek(), 2)
        self.assertEqual(len(s), 2)
        self.assertTrue(s)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)
        self.assertEqual(len(s), 0)
        self.assertFalse(s)

    def test_peek_does_not_remove(self):
        s = Stack()
        s.push("a")
        self.assertEqual(s.peek(), "a")
        self.assertEqual(len(s), 1)


if __name__ == "__main__":
    unittest.main()
