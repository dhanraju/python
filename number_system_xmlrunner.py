#!/usr/bin/env python
# coding: utf-8

import os
import unittest
import xmlrunner

def runner(output="test-reports/TEST-*.xml"):
	print("In runner.")
	return xmlrunner.XMLTestRunner(output=output)

def find_tests():
	print("In find_tests.")
	folders_list = []
	# folders_list = os.path.dirname(os.path.abspath(__file__))
	folders_list = os.path.dirname(__file__)
	print(folders_list)
	print(unittest.TestLoader().discover(folders_list, pattern="*_test.py"))
	return unittest.TestLoader().discover(folders_list, pattern="*_test.py")

if __name__ == '__main__':
	# Make sure the file __init__.py exists in every directory that have tests.
	print("start find_tests")
	runner().run(find_tests())
