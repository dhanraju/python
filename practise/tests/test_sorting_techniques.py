"""Pytest module to test sorting techniques."""
import os, sys

C_DIR = os.getcwd()
SRC_DIR = '%s/../programs/' % C_DIR

sys.path.append(SRC_DIR)
from sorting_techniques import SortingTechniques as SortObj

class TestSortingTechniques(object):
    """Test module to test sorting techniques."""

    @staticmethod
    def setup():
        """Setup."""
        print("setup class:Test")

    @staticmethod
    def teardown():
        """Teardown."""
        print("\n\nteardown class:Test")

    @classmethod
    def setup_class(cls):
        """Setup Class."""
        print("\nsetup_class class:%s" % cls.__name__)

    @classmethod
    def teardown_class(cls):
        """Teardown Class."""
        print("teardown_class class:%s" % cls.__name__)

    @classmethod
    def setup_method(cls, method):
        """Setup Method."""
        print("setup_method method:%s" % method.__name__)

    @classmethod
    def teardown_method(cls, method):
        """Teardown Method."""
        print("teardown_method method:%s" % method.__name__)

    def test_bubble_sort(self):
        """Test Bubble Sort."""
        print("\ntest_bubble_sort <====================== actual test code")
        list_obj = [5, 3, 4, 1, 2]
        assert SortObj.bubble_sort(list_obj) == [1, 2, 3, 4, 5]


'''
OUTPUT:
$ py.test -s test_sorting_techniques.py
==================================== test session starts
=====================================
platform linux2 -- Python 2.7.6 -- pytest-2.5.1
collected 1 items 

test_sorting_techniques.py 
setup_class class:TestSortingTechniques
setup_method method:test_bubble_sort
setup class:Test

test_bubble_sort <====================== actual test code
.

teardown class:Test
teardown_method method:test_bubble_sort
teardown_class class:TestSortingTechniques


================================== 1 passed in 0.01 seconds
==================================
'''
