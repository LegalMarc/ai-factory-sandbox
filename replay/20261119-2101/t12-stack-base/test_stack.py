import unittest

from stack import Stack


class TestStack(unittest.TestCase):
    def test_empty(self):
        s = Stack()
        self.assertEqual(len(s), 0)
        self.assertFalse(s)

    def test_push_pop(self):
        s = Stack()
        s.push(1)
        s.push(2)
        self.assertEqual(s.pop(), 2)
        self.assertEqual(s.pop(), 1)

    def test_peek(self):
        s = Stack()
        s.push("a")
        s.push("b")
        self.assertEqual(s.peek(), "b")
        self.assertEqual(len(s), 2)

    def test_pop_empty_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.pop()

    def test_peek_empty_raises(self):
        s = Stack()
        with self.assertRaises(IndexError):
            s.peek()

    def test_bool_and_len(self):
        s = Stack()
        self.assertFalse(bool(s))
        s.push(1)
        self.assertTrue(bool(s))
        self.assertEqual(len(s), 1)


if __name__ == "__main__":
    unittest.main()
