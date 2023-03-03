"""Unit tests for Merge overlappings intervals problem."""
from problem_solving import merge_overlap_intervals
import unittest


class TestMergeOverlapIntervals(unittest.TestCase):
    """Unit tests for Merge overlapping intervals problem."""
    def setUp(self):
        pass

    def test_merge_overlap(self):
        arr = [[1, 5], [3, 7], [4, 6], [6, 8]]
        actual_output = merge_overlap_intervals.merge_overlap_intervals(arr)
        expected_output = [1, 8]
        assert actual_output == expected_output


if __name__ == "__main__":
    unittest.main()