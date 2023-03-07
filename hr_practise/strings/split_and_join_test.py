"""Unit tests for split and join."""
from hr_practise.strings import split_and_join
import unittest


class TestSplitAndJoin(unittest.TestCase):
    """Unit tests for split and join problem."""
    def setUp(self):
        pass

    def test_split_and_join(self):
        given_string = "this is a string"
        expected_output = "this-is-a-string"
        actual_output = split_and_join.split_and_join(given_string)
        assert expected_output == actual_output

if __name__ == '__main__':
    unittest.main()