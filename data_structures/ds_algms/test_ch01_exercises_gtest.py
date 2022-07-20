import ch01_exercises
# from googletest.test import gtest_test_utils
import googletest


class TestCH01Exercises(googletest.TestCase):
  def setup(self):
    pass

  def testIsMultiplePositive(self):
    status = ch01_exercises.is_multiple(2, 8)
    print(status)
    assert status == True

  def testIsMultipleNegative(self):
    status = ch01_exercises.is_multiple(2, 7)
    print(status)
    assert status == False


if __name__ == '__main__':
    googletest.main()
