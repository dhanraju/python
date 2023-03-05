"""Unit tests for swap case problem."""
from hr_practise.strings import swap_case
import unittest

class TestSwapCase(unittest.TestCase):
    """Unit tests for swap case."""
    def setUP(self):
        pass

    def test_swap_case_01(self):
        given_string = "HackerRank.com presents \"Pythonist 2\"."
        expected_output = "hACKERrANK.COM PRESENTS \"pYTHONIST 2\"."
        actual_output = swap_case.swap_case(given_string)
        assert expected_output == actual_output

    def test_swap_case_02(self):
        given_string = "This IS a StRinG 2"
        expected_output = "tHIS is A sTrINg 2"
        actual_output = swap_case.swap_case(given_string)
        assert expected_output == actual_output


if __name__ == '__main__':
    unittest.main()