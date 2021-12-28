"""This module performs arithmetic operations.
Performing arithmetic operations demonstrates in two ways.
1. Functions as dictionary values.
2. Lambda forms as dictionary values.
"""

def add_two_nums(num1, num2):
    """Performs addition of two numbers."""
    return num1+num2

def mul_two_nums(num1, num2):
    """Performs multiplication of two numbers."""
    return num1*num2

def div_two_nums(num1, num2):
    """Performs division of two numbers."""
    return num1/num2

def mod_two_nums(num1, num2):
    """Performs modulo of two numbers."""
    return num1%num2

def sub_two_nums(num1, num2):
    """Performs subtraction of two numbers."""
    return num1-num2


DICT_OBJ = {
    1 : add_two_nums,
    2 : sub_two_nums,
    3 : mul_two_nums,
    4 : div_two_nums,
    5 : mod_two_nums
}

DICT_OBJ_LAMBDA = {
    1 : lambda num1, num2: num1+num2,
    2 : lambda num1, num2: num1-num2,
    3 : lambda num1, num2: num1*num2,
    4 : lambda num1, num2: num1/num2,
    5 : lambda num1, num2: num1%num2
}

def main():
    """Starting of the program."""
    print("Selecet an arithmetic operation from below menu:")
    print("1. Addition\n2. Subtraction\n3. Multiplication\n4. Division")
    print("5. Modulo")
    option = int(raw_input())

    print("Enter two numbers:")
    num1 = int(raw_input())
    num2 = int(raw_input())
    if option in DICT_OBJ.keys():
        print(DICT_OBJ[option](num1, num2))
        print("Solution using lamdba form: ", DICT_OBJ_LAMBDA[option](
	           num1, num2))

    # Lambda form demonstration.
    # print("Solution using lambda form"
        # for key_val in DICT_OBJ_LAMBDA:
        # print(DICT_OBJ_LAMBDA[key_val](num1, num2))


if __name__ == '__main__':
    main()
