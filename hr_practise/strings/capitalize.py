"""Capitalize the given line of string.

ensure that the first and last names of people begin with a capital letter in
their passports. For example, alison heck should be capitalised correctly as
Alison Heck.

Sample Input:
chris alan

Sample Output:
Chris Alan
"""

# import os

# Complete the solve function below.
def solve(s):
    split_str = s.split(' ')
    # Traverse through the list of strings.
    for i in range(len(split_str)):
        # Check the first character from the each list element is alphabet.
        if len(split_str[i]) > 0 and split_str[i][0].isalpha():
            if split_str[i][0].islower():
                split_str[i] = str(split_str[i][0].upper()) + str(
                    split_str[i][1:])
    return (' ').join(split_str)


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    print('given string = ', s)
    result = solve(s)
    print('result string = ', result)

    # fptr.write(result + '\n')

    # fptr.close()