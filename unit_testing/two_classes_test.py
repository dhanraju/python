from unit_testing import helloworld
import unittest

class TwoClassesTestBase(object):
    test_flag = None

    class TestHelloWorld(unittest.TestCase):
        @classmethod
        def setUpClass(self):
            print("In setUpClass, self.test_flag = %d" % self.test_flag)
            pass

        @classmethod
        def tearDownClass(self):
            print("In tearDownClass.")
            pass

        def test_helloworld(self):
            print("testing hello world.")
            st = 'Hello dhanu'
            ret_value = helloworld.helloworld(st)
            print("ret_value = ", ret_value)
            assert(ret_value == True)


class Class1Test(TwoClassesTestBase.TestHelloWorld):
    print("Class1Test.")
    test_flag = False


class Class2Test(TwoClassesTestBase.TestHelloWorld):
    print("Class2Test.")
    test_flag = True


if __name__ == '__main__':
    unittest.main()

# How to run:
# python two_classes_test.py
# Output:
'''
$ python two_classes_test.py 
Class1Test.
Class2Test.
In setUpClass, self.test_flag = 0
testing hello world.
Hello dhanu
ret_value =  True
.In tearDownClass.
In setUpClass, self.test_flag = 1
testing hello world.
Hello dhanu
ret_value =  True
.In tearDownClass.

----------------------------------------------------------------------
Ran 2 tests in 0.000s

OK
'''