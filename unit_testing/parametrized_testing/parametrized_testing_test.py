import pytest

@pytest.mark.parametrize("test_input, expected", [
	("3+5", 8),
	("2+4", 6),
#("6*9", 42)
])

def test_eval(test_input, expected):
	assert eval(test_input) == expected

'''
Ref: 
https://docs.pytest.org/en/latest/parametrize.html#parametrize-basics
https://docs.pytest.org/en/latest/example/parametrize.html
https://docs.pytest.org/en/latest/parametrize.html
https://eli.thegreenplace.net/2011/08/02/python-unit-testing-parametrized-test-cases
https://vilimpoc.org/blog/2013/07/12/python-parametrized-unit-tests/
https://medium.com/uckey/python-parameterized-module-is-useful-but-some-limitations-are-there-6afb034c8034
https://github.com/wolever/parameterized
https://technomilk.wordpress.com/2012/02/12/multiplying-python-unit-test-cases-with-different-sets-of-data/
http://tobyho.com/2009/03/12/parameterizing-your-tests/
https://gist.github.com/simonw/6aaab51f84f163f3a675
'''
