"""Unit tests for capitalize problem."""

from hr_practise.strings import capitalize
import unittest


class TestCapitalize(unittest.TestCase):
    """Unit tests."""
    def setUP(self):
        pass
    
    def test_solve_capitalize(self):
        given_string = 'hello   world  lol'
        expected_output = 'Hello   World  Lol'
        assert expected_output == capitalize.solve(given_string)


if __name__ == '__main__':
    unittest.main()