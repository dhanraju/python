"""Unit tests for the module map_character."""
import unittest
from map_character import map_character


class TestMapCharacter(unittest.TestCase):
    """Unit tests for Map character method."""
    def test_positive_result(self):
        str1 = "adba"
        str2 = "cbfc"
        self.assertTrue(map_character(str1, str2))

    def test_negative_result(self):
        str1 = "adba"
        str2 = "cbfv"
        self.assertFalse(map_character(str1, str2))


if __name__ == "__main__":
    unittest.main()
