'''This python module demonstrates different types of number system.'''

class Conversion(object):
    '''This class performs conversion of one number system to the other.'''

    def __init__(self):
        self.hexa_ns = {
            '0':0,
            '1':1,
            '2':2,
            '3':3,
            '4':4,
            '5':5,
            '6':6,
            '7':7,
            '8':8,
            '9':9,
            'A':10,
            'B':11,
            'C':12,
            'D':13,
            'E':14,
            'F':15,
        }

    def anybase_to_decimal(self, i_value, base):
        '''Convert any base number system to decimal number system.'''
        decimal_num = 0
        # TODO(dhanraju): Fix pylint error consider-using-enumerate.
        for i in range(len(i_value)):
            decimal_num += int(self.hexa_ns[i_value[i]]) * base**(len(i_value)-i-1)
        # print("Given number %s of base \'%d\' in decimal number is: %d" % (
        #    i_value, base, decimal_num))
        return decimal_num

    def decimal_to_anybase(self, i_value, base):
        '''Convert decimal number to any base number system.'''
        temp = int(i_value)
        converted_num = ''
        while base <= temp:
            # Retrieve appropriate dictionary key for a value.
            # print(self.hexa_ns.keys())
            # print(self.hexa_ns.values())
            # print(list(self.hexa_ns.keys())[4])
            # print(temp%base)
            # print(list(self.hexa_ns.values())[int(temp%base)])
            position_value = list(self.hexa_ns.keys())[list(self.hexa_ns.values())[int(temp%base)]]
            converted_num = position_value + converted_num
            temp /= base
        position_value = list(self.hexa_ns.keys())[list(self.hexa_ns.values())[int(temp%base)]]
        converted_num = position_value + converted_num
        # print("Given decimal number %s in base \'%d\' is: %s" % (
        #    i_value, base, converted_num))
        return converted_num

    def octal_to_binary(self, i_value):
        '''Convert octal number to binary number.'''
        # Convert octal to decimal.
        decimal_num = self.anybase_to_decimal(str(i_value), 8)
        # Convert decimal to binary.
        binary_num = self.decimal_to_anybase(decimal_num, 2)
        # print("Given octal number %s in binary is: %s" % (
        # i_value, binary_num))
        return binary_num

    def hexa_to_binary(self, i_value):
        '''Convert hexa number to binary number.'''
        # Convert hexa number to decimal.
        decimal_num = self.anybase_to_decimal(str(i_value), 16)
        # Convert decimal to binary.
        binary_num = self.decimal_to_anybase(decimal_num, 2)
        # print("Given hexa number %s in binary is: %s" % (i_value, binary_num))
        return binary_num

    def octal_to_hexa(self, i_value):
        '''Convert octal number to binary number.'''
        # Convert octal to decimal.
        decimal_num = self.anybase_to_decimal(str(i_value), 8)
        # Convert decimal to hexa number.
        hexa_num = self.decimal_to_anybase(decimal_num, 16)
        # print("Given octal number %s in binary is: %s" % (i_value, hexa_num))
        return hexa_num

    def hexa_to_octal(self, i_value):
        '''Convert hexa number to binary number.'''
        # Convert hexa to decimal.
        decimal_num = self.anybase_to_decimal(str(i_value), 16)
        # Convert decimal to octal.
        octal_num = self.decimal_to_anybase(decimal_num, 8)
        # print("Given hexa number %s in octal is: %s" % (i_value, octal_num))
        return octal_num


if __name__ == '__main__':
    # print("Number system: Conversion demonstration.")
    NUM_SYSTEM_CONVERSION = Conversion()
    NUM_SYSTEM_CONVERSION.anybase_to_decimal('101101', 2)
    NUM_SYSTEM_CONVERSION.anybase_to_decimal('565', 8)
    NUM_SYSTEM_CONVERSION.anybase_to_decimal('175', 16)
    NUM_SYSTEM_CONVERSION.anybase_to_decimal('ABC', 16)
    NUM_SYSTEM_CONVERSION.decimal_to_anybase('45', 2)
    NUM_SYSTEM_CONVERSION.decimal_to_anybase('373', 8)
    NUM_SYSTEM_CONVERSION.decimal_to_anybase('373', 16)
    NUM_SYSTEM_CONVERSION.decimal_to_anybase('2748', 16)
    NUM_SYSTEM_CONVERSION.octal_to_binary('565')
    NUM_SYSTEM_CONVERSION.hexa_to_binary('175')
    NUM_SYSTEM_CONVERSION.octal_to_hexa('565')
    NUM_SYSTEM_CONVERSION.hexa_to_octal('175')
