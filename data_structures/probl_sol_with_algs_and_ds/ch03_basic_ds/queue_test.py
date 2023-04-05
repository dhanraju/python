"""Unit tests for queue library."""
import unittest
from queue import Queue


class QueueTest(unittest.TestCase):
    """Unit tests for queue operations."""
    def setUp(self):
        self.queue_obj = Queue()
        self.queue_obj.items = [1, 2, 3, 4]

    def test_is_empty(self):
        """Test is_empty functionality."""
        temp_obj = Queue()
        assert temp_obj.is_empty() is True

    def test_enqueue(self):
        """Test enqueue operation."""
        temp_value = self.queue_obj.items[0]
        self.queue_obj.enqueue(5)
        assert temp_value != self.queue_obj.items[0]

    def test_dequeue(self):
        """Test dequeue operation."""
        temp_value = self.queue_obj.items[-1]
        dequeue_value = self.queue_obj.dequeue()
        assert temp_value is dequeue_value

    def test_size(self):
        """Test size operation."""
        assert len(self.queue_obj.items) is self.queue_obj.size()


if __name__ == '__main__':
    unittest.main()
