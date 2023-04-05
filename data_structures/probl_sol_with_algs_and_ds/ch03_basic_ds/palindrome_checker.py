"""Palindrome checker problem.

A palindrome is a string that reads the same forward and backward.
For eg: radar, madam, toot
"""
from deque import Deque


def palindrome_checker(a_string):
    """Checks the given string is palindrome or not."""
    char_queue = Deque()
    for ch in a_string:
        char_queue.add_rear(ch)

    still_equal = True

    while char_queue.size() > 1 and still_equal:
        first = char_queue.remove_front()
        last = char_queue.remove_rear()
        if first != last:
            still_equal = False
    return still_equal


if __name__ == '__main__':
    STRING_1 = "lsdkjfskf"
    STRING_2 = "radar"
    print(f'Is the given string {STRING_1} is palindrome?',
        palindrome_checker(STRING_1))
    print(f'Is the given string {STRING_2} is palindrome?',
        palindrome_checker(STRING_2))
