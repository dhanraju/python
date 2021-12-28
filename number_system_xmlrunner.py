# coding: utf-8

import unittest
import xmlrunner

def runner(output='test-reports'):
	print("In runner.")
	return xmlrunner.XMLTestRunner(output=output)

def find_tests():
	print("In find_tests.")
	return unittest.TestLoader().discover('maths', pattern='*_test.py')

if __name__ == '__main__':
	print("start find_tests")
	runner().run(find_tests())