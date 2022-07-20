"""Data structures and algorithms in python - chapter01 exercises."""

# ************* Reinforcement *************

# R-1.1 Write a short Python function, is multiple(n, m), that takes two
# integer values and returns True if n is a multiple of m, that is, n = mi for
# some integer i, and False otherwise.
def is_multiple(n, m):
  """Is n a multiple of m.

  Args:
    n: Integer value.
    m: Integer value.

  Returns:
    Bool value: True if n is a multiple of m, otherwise False.
  """
  # Check the given numbers are integer
  if m%n:
    print('%d is NOT a multiple of %d' % (n, m))
    return False
  print('%d is a multiple of %d' % (n, m))
  return True

# R-1.2 Write a short Python function, is even(k), that takes an integer value
# and returns True if k is even, and False otherwise. However, your function
# cannot use the multiplication, modulo, or division operators.
def is_even(n):
  """Is n an even integer.

  Args:
    n: Integer value.

  Returns:
    Bool value: True
  """
  # Convert the integer value to binary value.
  # Check if the last char is '0' for even and '1' for odd.
  if int(bin(n)[-1]):
    print('%d is NOT an even number' % n)
    return False
  print('%d is a even number' % n)
  return True


# R-1.3 Write a short Python function, minmax(data), that takes a sequence of
# one or more numbers, and returns the smallest and largest numbers, in the
# form of a tuple of length two. Do not use the built-in functions min or
# max in implementing your solution.


# R-1.4 Write a short Python function that takes a positive integer n and
# returns the sum of the squares of all the positive integers smaller than n.
def sum_of_squares(n):
  """Returns the sum of squares of all the positive integers smaller than n.

  Args:
    n : A positive integer number.

  Returns:
    result: An integer value.
  """
  result = i = 0
  while i < n:
    result += i
    i += 1
  return result


# R-1.5 Give a single command that computes the sum from Exercise R-1.4, rely-
# ing on Python’s comprehension syntax and the built-in sum function.
def sum_of_squares_using_comp(n):
  return sum(i for i in range(n))

# R-1.6 Write a short Python function that takes a positive integer n and
# returns the sum of the squares of all the odd positive integers smaller than
# n.
def sum_of_odd_squares(n):
  result = i = 0
  while i < n:
    if i%2 == 1:
      result += i
    i += 1
  return result

# R-1.7 Give a single command that computes the sum from Exercise R-1.6, rely-
# ing on Python’s comprehension syntax and the built-in sum function.
def sum_of_odd_squares_using_comp(n):
  return sum([i for i in range(n) if i%2 == 1])

# R-1.8 Python allows negative integers to be used as indices into a sequence,
# such as a string. If string s has length n, and expression s[k] is used for
# index −n ≤ k < 0, what is the equivalent index j ≥ 0 such that s[j] references
# the same element?
def string_index(data, index_k):
  return index_k + len(data)

# R-1.9 What parameters should be sent to the range constructor, to produce a
# range with values 50, 60, 70, 80?


# R-1.10 What parameters should be sent to the range constructor, to produce a
# range with values 8, 6, 4, 2, 0, −2, −4, −6, −8?


# R-1.11 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [1, 2, 4, 8, 16, 32, 64, 128, 256].
def demo_list_compre(list_len):
  print([ 2**i for i in range(0, list_len) ])

# R-1.12 Python’s random module includes a function choice(data) that returns a
# random element from a non-empty sequence. The random module in-
# cludes a more basic function randrange, with parameterization similar to
# the built-in range function, that return a random choice from the given
# range. Using only the randrange function, implement your own version
# of the choice function.



# ************* Creativity *************

# C-1.13 Write a pseudo-code description of a function that reverses a list of n
# integers, so that the numbers are listed in the opposite order than they
# were before, and compare this method to an equivalent Python function
# for doing the same thing.
# Solution: Pseudo-code
# Create an empty list variable called reversed_list.
# Access the given_list variable using negative indexing and append each value
# in the reversed_list.
# reversed_list = [given_list[-i] for i in range(1, len(given_list)+1)]

# C-1.14 Write a short Python function that takes a sequence of integer values
# and determines if there is a distinct pair of numbers in the sequence whose
# product is odd.
# Solution:


# C-1.15 Write a Python function that takes a sequence of numbers and determines
# if all the numbers are different from each other (that is, they are distinct).
def is_distinct(data):
  temp_dict = {}
  for i in data:
    print(i, temp_dict)
    if str(i) in temp_dict:
      print('Not a distinct')
      return False
    else:
      temp_dict.update({f'{i}': ''})
  print('The given sequence is distinct.')
  return True



# C-1.16 In our implementation of the scale function (page 25), the body of the
# loop executes the command data[j] = factor. We have discussed that numeric
# types are immutable, and that use of the = operator in this context causes
# the creation of a new instance (not the mutation of an existing instance).
# How is it still possible, then, that our implementation of scale changes the
# actual parameter sent by the caller?


# C-1.17 Had we implemented the scale function (page 25) as follows, does it
# work properly?
# def scale(data, factor):
#   for val in data:
#     val = factor
# Explain why or why not.


# C-1.18 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [0, 2, 6, 12, 20, 30, 42, 56, 72, 90].
def demo_list_comp(n):
  [i*(i+1) for i in range(n)]

# C-1.19 Demonstrate how to use Python’s list comprehension syntax to produce
# the list [ a , b , c , ..., z ], but without having to type all 26 such
# characters literally.
def demo_list_comp_alphabets():
  return [chr(i) for i in range(97, 123)]

# C-1.20 Python’s random module includes a function shuﬄe(data) that accepts a
# list of elements and randomly reorders the elements so that each possi-
# ble order occurs with equal probability. The random module includes a
# more basic function randint(a, b) that returns a uniformly random integer
# from a to b (including both endpoints). Using only the randint function,
# implement your own version of the shuﬄe function.


# C-1.21 Write a Python program that repeatedly reads lines from standard input
# until an EOFError is raised, and then outputs those lines in reverse order
# (a user can indicate end of input by typing ctrl-D).


# C-1.22 Write a short Python program that takes two arrays a and b of length n
# storing int values, and returns the dot product of a and b. That is, it
# returns an array c of length n such that
# c[i] = a[i] · b[i], for i = 0, . . . , n − 1.


# C-1.23 Give an example of a Python code fragment that attempts to write an
# element to a list based on an index that may be out of bounds. If that index
# is out of bounds, the program should catch the exception that results, and
# print the following error message:
# “Don’t try buffer overflow attacks in Python!”


# C-1.24 Write a short Python function that counts the number of vowels in a
# given character string.
def count_vowels(string_data):
  count = 0
  for i in list(string_data):
    if i in ['a', 'e', 'i', 'o', 'u']:
      count += 1
  return count


# C-1.25 Write a short Python function that takes a string s, representing a
# sentence, and returns a copy of the string with all punctuation removed. For
# example, if given the string "Let\'s try, Mike.", this function would return
# "Lets try Mike".
def remove_punctuation(string_data):
  temp_string = ""
  for i in list(st):
    if i in string.ascii_uppercase or i in string.ascii_lowercase or i == ' ':
      temp_string = temp_string + i
  print(temp_string)
  return temp_string

# C-1.26 Write a short program that takes as input three integers, a, b, and c,
# from the console and determines if they can be used in a correct arithmetic
# formula (in the given order), like “a + b = c,” “a = b − c,” or “a ∗ b = c.”
def arith_formula(a, b, c):
  if (a+b == c) and (b-c == a) and (a*b == c):
    print(
      'The given input a= %d b=%d and c=%d is a correct arithmetic formula' % (
        a, b, c))
  else:
    print(
      'The given input a= %d b=%d and c=%d is NOT an correct arith formula' % (
        a, b, c))

# C-1.27 In Section 1.8, we provided three different implementations of a
# generator that computes factors of a given integer. The third of those
# implementations, from page 41, was the most efﬁcient, but we noted that it
# did not yield the factors in increasing order. Modify the generator so that
# it reports factors in increasing order, while maintaining its general
# performance advantages.


# C-1.28 The p-norm of a vector v = (v 1 , v 2 , . . . , v n ) in n-dimensional
# space is deﬁned as
# 
# p
# v = v 1 p + v 2 p + · · · + v n p .
# For the special case of p = 2, this results in the traditional Euclidean
# norm, which represents the length of the vector. For example, the Eu-
# clidean norm of a two-dimensional
# with coordinates (4, 3) has a
# √
# √ vector √
# 2
# 2
# Euclidean norm of 4 + 3 = 16 + 9 = 25 = 5. Give an implemen-
# tation of a function named norm such that norm(v, p) returns the p-norm
# value of v and norm(v) returns the Euclidean norm of v. You may assume
# that v is a list of numbers.



# ************* Projects *************

# P-1.29 Write a Python program that outputs all possible strings formed by
# using the characters c , a , t , d , o , and g exactly once.


# P-1.30 Write a Python program that can take a positive integer greater than 2
# as input and write out the number of times one must repeatedly divide this
# number by 2 before getting a value less than 2.


# P-1.31 Write a Python program that can “make change.” Your program should
# take two numbers as input, one that is a monetary amount charged and the
# other that is a monetary amount given. It should then return the number
# of each kind of bill and coin to give back as change for the difference
# between the amount given and the amount charged. The values assigned
# to the bills and coins can be based on the monetary system of any current
# or former government. Try to design your program so that it returns as
# few bills and coins as possible.


# P-1.32 Write a Python program that can simulate a simple calculator, using the
# console as the exclusive input and output device. That is, each input to the
# calculator, be it a number, like 12.34 or 1034, or an operator, like + or =,
# can be done on a separate line. After each such input, you should output
# to the Python console what would be displayed on your calculator.


# P-1.33 Write a Python program that simulates a handheld calculator. Your pro-
# gram should process input from the Python console representing buttons
# that are “pushed,” and then output the contents of the screen after each op-
# eration is performed. Minimally, your calculator should be able to process
# the basic arithmetic operations and a reset/clear operation.


# P-1.34 A common punishment for school children is to write out a sentence mul-
# tiple times. Write a Python stand-alone program that will write out the
# following sentence one hundred times: “I will never spam my friends
# again.” Your program should number each of the sentences and it should
# make eight different random-looking typos.


# P-1.35 The birthday paradox says that the probability that two people in a
# room will have the same birthday is more than half, provided n, the number of
# people in the room, is more than 23. This property is not really a paradox,
# but many people ﬁnd it surprising. Design a Python program that can test
# this paradox by a series of experiments on randomly generated birthdays,
# which test this paradox for n = 5, 10, 15, 20, . . . , 100.


# P-1.36 Write a Python program that inputs a list of words, separated by
# white space, and outputs how many times each word appears in the list. You
# need not worry about efﬁciency at this point, however, as this topic is
# something that will be addressed later in this book.


def main():
    is_multiple(2, 6)
    # is_multiple(2, 5)


if __name__ == '__main__':
    main()
