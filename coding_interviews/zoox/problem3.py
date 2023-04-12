"""
You are given a simple regular expression which uses only one construct: character groups. Each character group is denoted as "[a1a2...an]", and matches any one of the characters a1, a2, ..., an. Character groups cannot be nested. The regular expression consists of one or several character groups. Your task is to output the lexicographically smallest string which matches this regular expression.

The input data consists of a single string. The length of the string is between 1 and 20 characters, inclusive. Each character of the string is a lower-case letter of English alphabet, or an opening or a closing square bracket [ or ]. The string will represent a valid sequence of one or more valid character groups. The characters inside one character group might not be listed in alphabetical order.

Example

input

[abc][zyx][e]

output

axe
"""

import sys

line = sys.stdin.readline()  # Do not remove this line, mandatory for test runs
# print(line) # printed output is used to review test results

# Convert the given line into list of sorted strings.
# [abc][zyx][e] --> ["abc", "xyz", "e"]
formatted_list = []
for st in line.split("[")[1:]:
  temp_str = st.split("]")
  if len(temp_str) > 1:
    formatted_list.append(''.join(sorted(temp_str[0])))

output = ''

for list_element in formatted_list:
    output = output + list_element[0]

print(output)
