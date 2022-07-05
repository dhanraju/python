import ch01_exercises
import unittest


class TestCH01Exercises(unittest.TestCase):
  def setUp(self):
    pass

  def test_is_multiple_positive(self):
    status = ch01_exercises.is_multiple(2, 8)
    print(status)
    assert status == True

  def test_is_multiple_negative(self):
    status = ch01_exercises.is_multiple(2, 7)
    print(status)
    assert status == False


if __name__ == '__main__':
    unittest.main()
