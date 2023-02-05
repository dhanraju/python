'''Unit tests for calculator.'''
import os
import sys

CURR_DIR = '%s' % os.getcwd()
sys.path.append(CURR_DIR)

from tests.calculator import Calculator
import unittest


class TestCalculator(unittest.TestCase):
    '''Test Calculator module.'''
    def setUp(self):
        self.calc = Calculator()

    def test_sum(self):
        '''Test sum operation.'''
        answer = self.calc.add(2, 4)
        self.assertEqual(answer, 6)


if __name__ == '__main__':
    unittest.main()

# Ref:
# https://semaphoreci.com/community/tutorials/getting-started-with-mocking-in-python

# How to run this file:
# py.test <file_name.py>
