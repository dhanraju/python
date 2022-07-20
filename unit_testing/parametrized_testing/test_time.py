'''Ref: https://docs.pytest.org/en/latest/example/parametrize.html'''
import pytest

from datetime import datetime, timedelta

testdata = [
    (datetime(2001, 12, 12), datetime(2001, 12, 11), timedelta(1)),
    (datetime(2001, 12, 11), datetime(2001, 12, 12), timedelta(-1)),
]


@pytest.mark.parametrize("a, b, expected", testdata)
def test_timedistance_v0(a, b, expected):
    diff = a - b
    assert diff == expected


@pytest.mark.parametrize("a, b, expected", testdata, ids=["forward", "backward"])
def test_timedistance_v1(a, b, expected):
    diff = a - b
    assert diff == expected


def idfn(val):
    if isinstance(val, (datetime, )):
        # note this wouldn't show any hours/minutes/seconds
        return val.strftime('%Y%m%d')

@pytest.mark.parametrize("a, b, expected", testdata, ids=idfn)
def test_timedistance_v2(a, b, expected):
    diff = a - b
    assert diff == expected

'''
@pytest.mark.parametrize("a, b, expected", [
     pytest.param(datetime(2001, 12, 12), datetime(2001, 12, 11),
                  timedelta(1), id='forward'),
     pytest.param(datetime(2001, 12, 11), datetime(2001, 12, 12),
                  timedelta(-1), id='backward'),
])
def test_timedistance_v3(a, b, expected):
    diff = a - b
    assert diff == expected
****
THE COMMENED PIECE OF CODE IS FAILING WITH ATTRIBUTE ERROR:
$ pytest test_time.py
========================================== test session starts ==========================================
platform linux2 -- Python 2.7.13, pytest-3.0.6, py-1.4.34, pluggy-0.4.0
rootdir: /usr/local/google/home/dhanrama/sample_code/git/dhanraju/python/unit_testing, inifile: 
collected 0 items / 1 errors 

================================================ ERRORS =================================================
_____________________________________ ERROR collecting test_time.py _____________________________________
test_time.py:35: in <module>
    pytest.param(datetime(2001, 12, 12), datetime(2001, 12, 11),
E   AttributeError: 'module' object has no attribute 'param'
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!! Interrupted: 1 errors during collection !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
======================================== 1 error in 0.09 seconds ========================================
'''