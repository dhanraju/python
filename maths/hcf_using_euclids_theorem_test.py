"""Tests for hcf_using_euclids_theorem."""
from maths import hcf_using_euclids_theorem
import unittest
import xmlrunner


class TestHCFUsingEuclidsTheorem(unittest.TestCase):

    def test_euclid_division(self):
        self.assertEqual(hcf_using_euclids_theorem.euclidDivision(60, 100), 20)

    def test_getHCF(self):
        self.assertEqual(hcf_using_euclids_theorem.getHCF(60, 100), 20)


'''
TODO
    print 'HCF (100, 60) = ', euclidDivision(60, 100)
    print 'HCF (90, 30) = ', euclidDivision(90, 30)
    print 'HCF (50, 70) = ', euclidDivision(50, 70)
    print 'HCF (96, 72) = ', euclidDivision(96, 72)
    print 'HCF (300, 550) = ', euclidDivision(300, 550)
    print 'HCF (1860, 2015) = ', euclidDivision(1860, 2015)

    print '***** Traditional way of finding HCF of two numbers. *****'
    print 'HCF (100, 60) = ', getHCF(60, 100)
    print 'HCF (90, 30) = ', getHCF(90, 30)
    print 'HCF (50, 70) = ', getHCF(50, 70)
    print 'HCF (96, 72) = ', getHCF(96, 72)
    print 'HCF (300, 550) = ', getHCF(300, 550)
    print 'HCF (1860, 2015) = ', getHCF(1860, 2015)

***** Euclid's Division Lemma Algorithm *****
HCF (100, 60) =  20
HCF (90, 30) =  30
HCF (50, 70) =  10
HCF (96, 72) =  24
HCF (300, 550) =  50
HCF (1860, 2015) =  155
***** Traditional way of finding HCF of two numbers. *****
HCF (100, 60) =  20
HCF (90, 30) =  30
HCF (50, 70) =  10
HCF (96, 72) =  24
HCF (300, 550) =  50
HCF (1860, 2015) =  155

'''