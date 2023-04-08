"""Convert the decimal number to any base."""
from data_structures.probl_sol_with_algs_and_ds.ch03_basic_ds.stack import Stack

r_stack = Stack()

def to_str(n, base):
    convert_string = "0123456789ABCDEF"
    while n > 0:
        if n < base:
            r_stack.push(convert_string[n])
        else:
            r_stack.push(convert_string[n % base])
        n = n // base
    res = ""
    while not r_stack.is_empty():
        res = res + str(r_stack.pop())
    return res


if __name__ == '__main__':
    NUM = 1453
    BASE = 6
    print(f'Conversion of decimal number {NUM} to base {BASE} is',
        to_str(NUM, BASE))
