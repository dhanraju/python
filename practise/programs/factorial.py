"""This module does factorial of a given number."""


# Method 1: Simple logic to find factorial of given number.
def factorial_of_num(num):
    """Returns factorial of a given number."""
    fact = 1
    for i in range(1, num+1):
        fact *= i
    print('factorial of number ', num, ' is ', fact)
    return fact


# Method 2: Find factorial of given number using recursive technique.
def factorial_of_num_recursive(num):
    """Recursive logic implemented and returns factorial of a given number."""
    if num == 0:
        return 1
    return num * factorial_of_num_recursive(num-1)


def main():
    """Starting of the program."""
    print("Enter a number to find its factorial:")
    num = int(raw_input())
    print("The factorial of given number '%d' is '%d'" % (
        num, factorial_of_num(num)))
    print("The factorial of given number using recursive '%d' is '%d'" % (
        num, factorial_of_num_recursive(num)))


if __name__ == '__main__':
    main()
