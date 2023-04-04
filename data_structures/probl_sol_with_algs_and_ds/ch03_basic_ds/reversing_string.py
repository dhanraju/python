"""Question:

Write a function rev_string(my_str) that uses a stack to reverse the characters
in a string.
"""
from stack import Stack


def rev_string(my_str):
    """Reverse the characters in a string by using stack."""
    reverse_str = Stack()
    for c in my_str:
        reverse_str.push(c)
    return ''.join(reverse_str.items)

if __name__ == '__main__':
    print(rev_string('DhanRaj'))
