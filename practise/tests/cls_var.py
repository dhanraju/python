'''Ref:
https://stackoverflow.com/questions/7554738/python-self-no-self-and-cls'''
from unittest import TestCase

class ClassA(object):
    # var_a = 'hello'

    class ClassAB(TestCase):
        @classmethod
        def setUpClass(cls):
            print("in setUpClass: ", cls.var_a)
            print("junk in ClassAB")
        def method01(self):
            print("in classAB method01")
        def run_test(self):
            print("run_test, self.var_a = ", self.var_a)
        def test_ab(self):
            print("test_ab")
            self.run_test()
            self.assertEqual(True, True)

class ClassB(ClassA.ClassAB):
    var_a = 'hi'

class ClassC(ClassA.ClassAB):
    var_a = 'what'


'''
$ py.test -s cls_var.py
========================================= test session starts =========================================
platform linux2 -- Python 2.7.6 -- pytest-2.5.1
collected 2 items 

cls_var.py in setUpClass:  hi
junk in ClassAB
test_ab
run_test, self.var_a =  hi
.in setUpClass:  what
junk in ClassAB
test_ab
run_test, self.var_a =  what
.

====================================== 2 passed in 0.08 seconds =======================================
'''
