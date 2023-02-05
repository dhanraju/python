'''Unit test using mock.'''
import os
import sys

CURR_DIR = '%s' % os.getcwd()
sys.path.append(CURR_DIR)

from calculator import Calculator
import unittest
from unittest.mock import patch


class TestCalculator(unittest.TestCase):
    '''Test Calculator module.'''

    @patch('mocking.calculator.Calculator.add', return_value=5)
    def test_sum(self, add):
        self.assertEqual(add(2, 3), 5)


if __name__ == "__main__":
    unittest.main()

# Ref:
# https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python

# How to run this file:
# py.test <file_name.py>


# Other Refs:
# https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
# https://docs.python.org/3/library/unittest.mock-examples.html
# https://myadventuresincoding.wordpress.com/2011/02/26/python-python-mock-cheat-sheet/
# http://www.alexandrejoseph.com/blog/2015-08-21-python-mock-example.html
# https://www.programcreek.com/python/example/15532/mock.side_effect
# https://blog.fugue.co/2016-02-11-python-mocking-101.html

