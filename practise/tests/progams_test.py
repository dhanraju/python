"""Pytest module to test programs present programs folder.

How to run:
Navigate to tests directory and run py.test test_programs.py
"""

import os, sys

C_DIR = os.getcwd()
SRC_DIR = '%s/../programs/' % C_DIR

sys.path.append(SRC_DIR)
from practise.programs import factorial as FactObj
from practise.programs import fibonacci as FiboObj

def test_factorial():
    """Tests factorial of a number."""
    print("inside test_factorial")
    assert FactObj.factorial_of_num(4) == 24

def test_fibonacci():
    """pytest to verify fibonacci series."""
    print("inside test_fibonacci")
    assert FiboObj.fibonacci_series(5) == [0, 1, 1, 2, 3, 5]


'''
OUTPUT:
$ py.test test_programs.py
==================================== test session starts
=====================================
platform linux2 -- Python 2.7.6 -- pytest-2.5.1
collected 2 items 

test_programs.py ..

================================== 2 passed in 0.01 seconds
==================================
'''
