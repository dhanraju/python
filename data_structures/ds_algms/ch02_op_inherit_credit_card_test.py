"""Unit tests for PredatoryCreditCard which is an inheritance of Creditcard."""

import unittest
from data_structures.ds_algms.ch02_op_inherit_credit_card import PredatoryCreditCard


class Test02PredatoryCreditCard(unittest.TestCase):

    def setUp(self):
        self.predatory_cc_obj = PredatoryCreditCard(
            'John Bowman', 'California Savings',
            '5391 0375 9387 5309', 1, 2)

    def test_charge_success(self):
        success = self.predatory_cc_obj.charge(2)
        assert success == False