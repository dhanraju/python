from hr_practise.collections import company_logo
import unittest


class TestCompanyLogo(unittest.TestCase):
    """Unit tests for company logo problem."""
    def setUp(self):
        pass
    
    def test_company_logo(self):
        given_string = 'qwertyuiopasdfghjklzxcvbnm'  # 'aabbbccde'
        sorted_values = company_logo.sort_char_occurrence_count(given_string)
        print(sorted_values, '<-----')
        # assert (sorted_values == {'b' : 3, 'a' : 2, 'c' : 2})
        assert (sorted_values == {'a' : 1, 'b' : 1, 'c' : 1})


if __name__ == "__main__":
    unittest.main()