from maths import number_system
import unittest

class TestNumberSystemConversion(unittest.TestCase):
    def setUp(self):
    	self.conversion = number_system.Conversion()

    def test_anybase_to_decimal_01(self):
        ret_value = self.conversion.anybase_to_decimal("101101", 2)
        print("ret_value = ", ret_value)
        assert(ret_value == 45)

    def test_anybase_to_decimal_02(self):
        ret_value = self.conversion.anybase_to_decimal("565", 8)
        print("ret_value = ", ret_value)
        assert(ret_value == 373)

    def test_anybase_to_decimal_03(self):
        ret_value = self.conversion.anybase_to_decimal("175", 16)
        print("ret_value = ", ret_value)
        assert(ret_value == 373)

    def test_anybase_to_decimal_04(self):
        ret_value = self.conversion.anybase_to_decimal("ABC", 16)
        print("ret_value = ", ret_value)
        assert(ret_value == 2748)

    '''def test_decimal_to_anybase_01(self):
        ret_value = self.conversion.decimal_to_anybase("45", 2)
        print("ret_value = ", ret_value)
        assert(ret_value == "101101")

    def test_decimal_to_anybase_02(self):
        ret_value = self.conversion.decimal_to_anybase("373", 8)
        print("ret_value = ", ret_value)
        assert(ret_value == "565")

    def test_decimal_to_anybase_03(self):
        ret_value = self.conversion.decimal_to_anybase("373", 16)
        print("ret_value = ", ret_value)
        assert(ret_value == "175")

    def test_decimal_to_anybase_04(self):
        ret_value = self.conversion.decimal_to_anybase("2748", 16)
        print("ret_value = ", ret_value)
        assert(ret_value == "ABC")'''

    def test_octal_to_binary(self):
        ret_value = self.conversion.octal_to_binary("565")
        print("ret_value = ", ret_value)
        assert(ret_value == "101110101")

    def test_hexa_to_binary(self):
        ret_value = self.conversion.hexa_to_binary("175")
        print("ret_value = ", ret_value)
        assert(ret_value == "101110101")

    def test_octal_to_hexa(self):
        ret_value = self.conversion.octal_to_hexa("565")
        print("ret_value = ", ret_value)
        assert(ret_value == "175")

    def test_hexa_to_octal(self):
        ret_value = self.conversion.hexa_to_octal("175")
        print("ret_value = ", ret_value)
        assert(ret_value == "565")


if __name__ == '__main__':
    unittest.main()
