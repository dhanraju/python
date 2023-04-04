"""Convert decimal number to any base."""

from stack import Stack


def base_converter(decimal_number, base):
    """Convert decimal number number to any base number.
    
    Devide the decimal number with the base using % operator and push the
    quotient to the stack. Now divide the decimal number using // operator
    and use the reminder for further conversion.
    """
    digits = "0123456789ABCDEF"
    quotient_stack = Stack()
    reminder = decimal_number
    while reminder > 0:
        quotient = reminder % base
        quotient_stack.push(quotient)
        reminder = reminder // base

    new_string = ""
    while not quotient_stack.is_empty():
        new_string = new_string + digits[quotient_stack.pop()]
    return new_string


if __name__ == '__main__':
    dec_num = 25
    b = 2
    print(f'Base conversion of decimal number {dec_num} to base {b} is',
        base_converter(dec_num, b))
    base = 8
    print(f'Base conversion of decimal number {dec_num} to base {b} is',
        base_converter(dec_num, 8))
    dec_num = 256
    print(f'Base conversion of decimal number {dec_num} to base {b} is',
        base_converter(dec_num, 16))
    dec_num = 26
    print(f'Base conversion of decimal number {dec_num} to base {b} is',
        base_converter(26, 26)) # Not sure this works correctly.
