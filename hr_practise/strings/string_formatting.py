"""String formatting problem - Number system conversion.

Given an integer, n, print the following values for each integer i from 1 to n:
1. Decimal
2. Octal
3. Hexadecimal (capitalized)
4. Binary

Function Description:
Complete the print_formatted function in the editor below.

print_formatted has the following parameters:
int number: the maximum value to print
Prints

The four values must be printed on a single line in the order specified above
for each i from 1 to number. Each value should be space-padded to match the
width of the binary value of  and the values should be separated by a single
space.

Input Format:
A single integer denoting n.

Constraints:
* 1 <= n <= 99
"""
HEX_NUM = {
    '10': 'A',
    '11': 'B',
    '12': 'C',
    '13': 'D',
    '14': 'E',
    '15': 'F',
}

def num_sys_conversion(num_sys, num):
    """ Converts the given number in to the given number system.
    
    This method uses the prime factorization technique for the conversion.
    For example:
    The given integer is 27 and the procedure to convert it to hexa decimal
    system is as follows:
    16|27
    16|1 - 11 (-> 'B' which is quotient)
      |0 - 1  (-> 1)
    Result after conversion = 1B
    """
    conv_num = ''
    remainder = num
    while remainder >= 1:
        quotient = remainder%num_sys
        if num_sys == 16:
            if quotient > 9:
                conv_num = HEX_NUM[str(quotient)] + conv_num
            elif remainder > 9 and remainder < num_sys:
                conv_num = HEX_NUM[str(remainder)] + conv_num
            else:
                conv_num = str(quotient) + conv_num
        else:
            conv_num = str(quotient) + conv_num
        remainder = remainder//num_sys
    return conv_num

def print_formatted(number):
    # your code goes here
    ret_string = []
    type(ret_string)
    # Get the width of the binary.
    width = len(str(num_sys_conversion(2, number)))
    for i in range(1, number+1):
        print(str(num_sys_conversion(10, i)).rjust(width),
              str(num_sys_conversion(8, i)).rjust(width),
              str(num_sys_conversion(16, i)).rjust(width),
              str(num_sys_conversion(2, i)).rjust(width)
              )


if __name__ == '__main__':
    n = int(input())
    print_formatted(n)