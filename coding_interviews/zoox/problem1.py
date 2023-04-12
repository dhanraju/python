"""
Problem Description
You are working at Zoox to track autonomous vehicle miles driven.  The data is provided as a list of numbers, where each number represents the amount of autonomous miles driven for a particular day.  Occasionally, the measurement erroneously provides a negative number, which should be ignored.

Write a program that calculates the average autonomous miles driven and prints this value, or 0 if there were no miles driven.

Example
input

1,7,4,-3,-1,-2,1,6

output

3.8
"""

import sys

line = sys.stdin.readline()  # Do not remove this line, mandatory for test runs
# print(line) # printed output is used to review test results
total = 0
count = 0
for num in line.split(','):
  if int(num) > 0:
    total = total + int(num)
    count = count + 1

print(total/count)