"""Tuples problem unit tests."""

from hr_practise.basic_data_types import tuples_hashing
import unittest


class TestTuplesHashing(unittest.TestCase):
    """Unit tests for tuples problem."""
    def setUp(self):
        pass
    
    def test_get_hash_value(self):
        hash_value = tuples_hashing.get_hash_value(
            2, tuple(map(int, '1 2'.split())))
        print(hash_value)
        assert hash_value == '-3550055125485641917'


if __name__ == '__main__':
    unittest.main()