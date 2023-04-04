"""Unit tests for stack module."""
import unittest
from stack import Stack


class StackTest(unittest.TestCase):
    """Unit tests for stack library."""
    def setUp(self):
        self.stack_obj = Stack()
        self.stack_obj.items = [1, 2, 3, 4]

    def test_push(self):
        """Test push operation."""
        push_value = 5
        self.stack_obj.push(push_value)
        new_lifo_value = self.stack_obj.items[0]
        assert new_lifo_value == push_value

    def test_pop(self):
        """Test pop operation."""
        current_stack = self.stack_obj.items
        assert self.stack_obj.pop() != current_stack

    def test_size(self):
        """Test size operation."""
        assert len(self.stack_obj.items) == self.stack_obj.size()

    def test_is_empty(self):
        """Test is empty operation."""
        stack_items = self.stack_obj.items
        assert (not stack_items) == self.stack_obj.is_empty()

    def test_peek(self):
        """Test peek operation."""
        lifo_value = self.stack_obj.items[0]
        assert lifo_value == self.stack_obj.peek()


if __name__ == '__main__':
    unittest.main()
