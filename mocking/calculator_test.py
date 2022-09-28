'''Unit tests for calculator.'''
import os
import sys

import unittest
from mocking.calculator import Calculator

CURR_DIR = '%s' % os.getcwd()

sys.path.append(CURR_DIR)


class TestCalculator(unittest.TestCase):
    '''Test Calculator module.'''
    # def setUp(self):
    #    self.calc = Calculator()

    @patch('main.Calculator.sum', return_value=6)
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
