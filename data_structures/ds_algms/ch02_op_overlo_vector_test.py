import unittest
from ch02_op_overlo_vector import Vector


_VECTOR_3D = 3


class OpOverLoVectorTest(unittest.TestCase):
  def setUp(self):
    # Initialize vector_a and vector_b with values and create resultant vector.
    self.vector_a = self.vector_b = self.vector_c = Vector(_VECTOR_3D)
    vector_a[0] = 1
    vector_a[1] = 2
    vector_a[2] = 3
    vector_b[0] = 4
    vector_b[1] = 5
    vector_b[2] = 6

  def test_vector_init(self):
    vector_a = Vector(_VECTOR_3D)
    assert str(vector_a) == '<0, 0, 0>'

  def test_len(self):
    vector_a = Vector(_VECTOR_3D)
    assert len(vector_a) == _VECTOR_3D


if __name__ == "__main__":
  unittest.main()