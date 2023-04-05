"""Unit tests for unordered lists."""
import unittest
from unordered_lists import UnorderedList


class UnorderedListTest(unittest.TestCase):
    """Unit tests for underordered list operations."""
    def setUp(self):
        """Initialiaze the underordered list object."""
        self.unordered_list_obj = UnorderedList()
        self.unordered_list_obj.add(1)
        self.unordered_list_obj.add(2)
        self.unordered_list_obj.add(3)
        self.unordered_list_obj.add(4)

    def test_size(self):
        """Test size operation."""
        temp_list = UnorderedList()
        temp_list.add(1)
        temp_list.add(2)
        temp_list.add(3)
        temp_list.add(4)
        assert temp_list.size() is 4

    def test_is_empty(self):
        """Test is_empty operation."""
        temp_list = UnorderedList()
        temp_list.add(1)
        temp_list.add(2)
        assert temp_list.is_empty is not None

    def test_search(self):
        """Test search operation."""
        assert self.unordered_list_obj.search(3) is True

    def test_remove(self):
        """Test remove operation."""
        self.unordered_list_obj.remove(4)
        assert self.unordered_list_obj.search(4) is False


if __name__ == '__main__':
    unittest.main()
