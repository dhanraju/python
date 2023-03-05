"""Unit tests for list comprehensions problem."""
from hr_practise.basic_data_types import list_comps
import unittest


class TestListComps(unittest.TestCase):
    """Unit tests for list comprehensions problem."""
    def setUp(self):
        pass
    
    def test_with_data_01(self):
        x = 1
        y = 1
        z = 1
        n = 2
        expected_output = [
            [0, 0, 0], [0, 0, 1], [0, 1, 0], [1, 0, 0], [1, 1, 1]]
        actual_output = list_comps.get_possible_coordinates(x, y, z, n)
        assert expected_output ==  actual_output

    def test_with_data_02(self):
        x = 2
        y = 2
        z = 2
        n = 2
        expected_output = [
            [0, 0, 0], [0, 0, 1], [0, 1, 0], [0, 1, 2], [0, 2, 1],
            [0, 2, 2], [1, 0, 0], [1, 0, 2], [1, 1, 1], [1, 1, 2],
            [1, 2, 0], [1, 2, 1], [1, 2, 2], [2, 0, 1], [2, 0, 2],
            [2, 1, 0], [2, 1, 1], [2, 1, 2], [2, 2, 0], [2, 2, 1],
            [2, 2, 2]]
        actual_output = list_comps.get_possible_coordinates(x, y, z, n)
        assert expected_output ==  actual_output


if __name__ == '__main__':
    unittest.main()