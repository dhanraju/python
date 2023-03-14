import unittest
from data_structures.ds_algms.ch02_op_overlo_vector import Vector


_VECTOR_3D = 3


class OpOverLoVectorTest(unittest.TestCase):
  def setUp(self):
    # Initialize vector_a and vector_b with values and create resultant vector.
    # print("In setUp of OpOverLoVectorTest")
    pass

  def test_vector_init(self):
    vector_a = Vector(_VECTOR_3D)
    assert str(vector_a) == '<0, 0, 0>'

  def test_len(self):
    vector_a = Vector(_VECTOR_3D)
    assert len(vector_a) == _VECTOR_3D


if __name__ == "__main__":
  unittest.main()