"""Unit tests for finding the runner up score problem."""
from hr_practise.basic_data_types import runner_up_score
import unittest

class TestFindRunnerUpScore(unittest.TestCase):
    """Unit tests for Find Runner-Up Score."""
    def setUp(self):
        pass

    def test_find_runner_up_score(self):
        arr = [2, 3, 6, 6, 5]
        expected_output = 5
        actual_output = runner_up_score.find_runner_up_score(arr)
        assert expected_output == actual_output


if __name__ == '__main__':
    unittest.main()