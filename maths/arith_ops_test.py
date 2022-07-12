import unittest
from arith_ops import ArithOps

class ArithOpsTest(unittest.TestCase):
  def setUp(self):
    self.arith_ops_obj = ArithOps()

  def test_add(self):
    assert self.arith_ops_obj.add(3, 4) == 7

  def test_sub(self):
    assert self.arith_ops_obj.sub(5, 2) == 3