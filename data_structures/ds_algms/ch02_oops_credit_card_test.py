"""Test cases for chapter02 program of credit card module."""
import unittest
# from data_structures.ds_algms.ch02_oops_credit_card import CreditCard

class TestCh02CreditCard(unittest.TestCase):
  """Unit test cases for the module CreditCard."""
  def setUp(self):
    self.wallet = []
    self.wallet.append(
      CreditCard('John Bowman', 'California Savings',
        '5391 0375 9387 5309', 2500))
    self.wallet.append(
      CreditCard('Dhan', 'California Federal',
        '3485 0399 3395 1954', 91))
    self.wallet.append(
      CreditCard('Raj', 'California Finance',
        '5391 0375 9387 5309', 101))

  # Method coverage unit tests.
  def test_get_customer(self):
    assert self.wallet[0].get_customer() == 'John Bowman'

  def test_get_limit(self):
    # print(self.wallet[1].get_limit())
    assert self.wallet[1].get_limit() == 91

  def test_get_bank(self):
    assert self.wallet[2].get_bank() == 'California Finance'

  def test_get_acnt(self):
    assert self.wallet[0].get_account() == '5391 0375 9387 5309'

  # Statement coverage unit tests.
  def test_charge_lower_limit(self):
    assert self.wallet[1].charge(10) == True

  def test_charge_upper_limit(self):
    assert self.wallet[0].charge(2505) == False

  def test_make_payment(self):
    if self.wallet[2].get_balance() == 0:
      self.wallet[2].charge(100)
      self.wallet[2].make_payment(50)
    assert self.wallet[2].get_balance() == 50


if __name__ == "__main__":
    unittest.main()