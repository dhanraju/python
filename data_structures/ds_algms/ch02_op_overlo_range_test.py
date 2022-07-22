"""Unit tests for ch02_op_overlo_range module."""
import unittest
from data_structures.ds_algms.ch02_op_overlo_range import Range


class TestRange(unittest.TestCase):

    def setUp(self):
        self.range_var = Range(6)

    def test_range_len(self):
        assert len(self.range_var) == 6

    def test_range_getitem_only_stop_val(self):
        expected_list = [0, 1, 2, 3, 4]
        result_list = []
        for i in Range(5):
            result_list.append(i)
        assert result_list == expected_list

    def test_range_getitem_start_stop_val(self):
        expected_list = [5, 6, 7, 8, 9]
        result_list = []
        for i in Range(5, 10):
            result_list.append(i)
        assert result_list == expected_list

    def test_range_getitem_start_stop_step(self):
        expected_list = [0, 5, 10, 15, 20]
        result_list = []
        for i in Range(0, 25, 5):
            result_list.append(i)
        assert result_list == expected_list


if __name__ == "__main__":
    unittest.main()