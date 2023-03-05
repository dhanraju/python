"""Unit tests for Finding the percentage."""

from hr_practise.basic_data_types import finding_percentage
import unittest


class TestFindingPercentage(unittest.TestCase):
    """Unit tests for finding percentage problem."""
    def setUp(self):
        pass

    def test_finding_percentage_01(self):
        student_marks = {
            'Krishna': [67, 68, 69],
            'Arjun': [70, 98, 63],
            'Malika': [52, 56, 60]
        }
        query_name = 'Malika'
        expected_output = 56.00
        actual_output = finding_percentage.find_percentage(
            student_marks, query_name)

    def test_finding_percentage_02(self):
        student_marks = {
            'Harsh': [25, 26.5, 28],
            'Anurag': [26, 28, 30],
        }
        query_name = 'Harsh'
        expected_output = 26.50
        actual_output = finding_percentage.find_percentage(
            student_marks, query_name)


if __name__ == '__main__':
    unittest.main()