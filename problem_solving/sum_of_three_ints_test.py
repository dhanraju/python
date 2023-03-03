"""Unit tests for sum_of_three_ints problem."""
from problem_solving import sum_of_three_ints
import unittest


class TestSumOfThreeInts(unittest.TestCase):
    """Tests for sum of three ints problem."""
    def setUp(self):
        pass
    
    def test_array_values(self):
        arr = [5, 6, 9, 8, 3, 2, 7, 4, 1]
        value = 20
        expected_output = [[5, 6, 9], [5, 8, 7], [9, 8, 3], [9, 7, 4]]
        actual_output = sum_of_three_ints.sum_of_three_ints(arr, value)
        assert actual_output == expected_output


if __name__ == "__main__":
    unittest.main()