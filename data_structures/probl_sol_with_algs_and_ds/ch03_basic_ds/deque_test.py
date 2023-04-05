"""Unit tests for deque."""

import unittest
from deque import Deque


class DequeTest(unittest.TestCase):
    """Unit tests for Deque operations."""
    def setUp(self):
        """Initialize deque object."""
        self.deque_obj = Deque()
        self.deque_obj.items = [1, 2, 3, 4]

    def test_add_front(self):
        """Test for add at front operation."""
        value = 5
        self.deque_obj.add_front(value)
        assert self.deque_obj.items[-1] is value

    def test_add_rear(self):
        """Test for add at rear operation."""
        value = 6
        self.deque_obj.add_rear(value)
        assert self.deque_obj.items[0] is value

    def test_remove_front(self):
        """Test for remove at front operation."""
        removed_item = self.deque_obj.remove_front()
        assert removed_item is not self.deque_obj.items[-1]

    def test_remove_rear(self):
        """Test for remove at rear operation."""
        removed_item = self.deque_obj.remove_rear()
        assert removed_item is not self.deque_obj.items[0]


if __name__ == '__main__':
    unittest.main()
