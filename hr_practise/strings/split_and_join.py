"""String split and join.

You are given a string. Split the string on a " " (space) delimiter and join
using a - hyphen.

Input Format:
The one line contains a string consisting of space separated words.

Output Format:
The space delimiter should be repalced with - hypen.
"""

def split_and_join(line):
    # write your code here
    return '-'.join(line.split(' '))

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)