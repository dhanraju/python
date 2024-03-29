"""Swap case problem.

You are given a string and your task is to swap cases. In other words, convert
all lowercase letters to uppercase letters and vice versa.

For Example:
Www.HackerRank.com -> wWW.hACKERrANK.COM
Pythonist 2 -> pYTHONIST 2
"""

def swap_case(s):
    return ''.join([c.upper() if c.islower() else c.lower() for c in s])

if __name__ == '__main__':
    s = input()
    result = swap_case(s)
    print(result)