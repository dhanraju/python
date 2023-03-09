"""Unit tests for string formatting problem."""
from hr_practise.strings import string_formatting
import unittest

class TestStringFormatting(unittest.TestCase):
    """Unit tests for string formatting."""
    def setUp(self):
        pass
    
    def test_num_sys_conversion(self):
        assert '1B' == string_formatting.num_sys_conversion(16, 27)


if __name__ == '__main__':
    unittest.main()