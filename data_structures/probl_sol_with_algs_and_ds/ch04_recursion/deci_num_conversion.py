"""Convert an integer to a string.

Convert the given integer to a string in any base between binary and
hexadecimal.
"""

def to_str(num, base):
    convert_string = "0123456789ABCDEF"
    if num < base:
        return convert_string[int(num)]
    return to_str(num/base, base) + convert_string[ int(num%base) ]


if __name__ == '__main__':
    GIVEN_NUM = 1453
    BASE = 16
    print(f'Convertion of given num {GIVEN_NUM} to base {BASE} is',
        to_str(GIVEN_NUM, BASE))
