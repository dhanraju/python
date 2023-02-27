from hr_practise.basic_data_types import nested_lists
import unittest

class TestNestedLists(unittest.TestCase):
    """Unit tests for nested lists problem."""
    def setUp(self):
        pass

    def test_second_lowest_grade_tc01(self):
        '''student_record = [
            ["Harry", 37.21],
            ["Berry", 37.21],
            ["Tina", 37.2],
            ["Akriti", 41],
            ["Harsh", 39],
        ]'''
        student_record = [["Prashant", 32], ["Pallavi", 36], ["Dheeraj", 39], ["Shivam", 40]]
        print(nested_lists.second_lowest_grade(student_record))
        # assert (["Berry", "Harry"] == nested_lists.second_lowest_grade(student_record))
        assert (["Pallavi"] == nested_lists.second_lowest_grade(student_record))


if __name__ == "__main__":
    unittest.main()


# Other test data
# ["Prashant", 32], ["Pallavi, 36], ["Dheeraj", 39], ["Shivam", 40]