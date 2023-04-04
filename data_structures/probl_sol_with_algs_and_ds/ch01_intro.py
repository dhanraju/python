"""Chapter 1 Exercises."""

def gcd(m, n):
    """Calculate gcd of a fraction.

    The GCD will be calculated using Euclid's theorem. It states that, the
    greatest common divisor of two integers m and n is n if n divides m
    evenly. However, if n doesn't divide m evenly, then the answer is the
    greatest command divisor of n and the reminder of m divided by n.
    """
    while m % n != 0:
        old_m = m
        old_n = n
        m = old_n
        n = old_m % old_n
    return n


class FailException(Exception):
    """Exception message for a failed test."""
    def __init__(self, fail_message):
        self.message = fail_message

    def __str__(self):
        return str(self.message)


class Fraction:
    """Initialize the fraction base class."""
    def __init__(self, top, bottom):
        """Initiaze the object by passing numerator and denominator of
        a fraction."""
        self.num = top
        self.den = bottom
        # Exercise 5.
        # Modify the constructor for the fraction class so that it checks to
        # make sure that the numerator and denominator are both integers. If
        # either is not an integer the constructor should raise an exception.
        if not isinstance(self.num, int):
            raise FailException(
                f'Numerator of type %s is not an int type!' % type(self.num))
        if not isinstance(self.den, int):
            raise FailException(
                f'Denominator of type %s is not an int type!' % type(self.den))
        # Get the greated command divisor of the fraction.
        common_div = gcd(self.num, self.den)
        print('The gcd is = ', common_div)
        # Update the num and den values with common divisor.
        self.num = self.num//common_div
        self.den = self.den//common_div


class FractionEx01(Fraction):
    """Exercise 1.

    Implement the simple methods get_num and get_den that will return the
    numerator and denominator of a fraction.
    """
    def get_num(self):
        """Returns numerator of a fraction."""
        return self.num

    def get_den(self):
        """Returns denominator of a fraction."""
        return self.den


class FractionEx02(FractionEx01):
    """Exercise 2.

    In many ways it would be better if all fractions were maintained in lowest
    terms right from the start. Modify the constructor for the Fraction class
    so that GCD is used to reduce fractions immediately. Notice that this means
    the __add__ function no longer needs to reduce. Make the necessary
    modifications.
    """
    def __add__(self, another_fraction):
        """Operator over loading for addition operation.

        __add__ function is one of the magic methods in python and returns the
        object of type same as input objects. obj3 = obj1.__add__(self, obj2)

        Args:
          another_fraction: (object) Fraction object type.

        Returns:
          result_fraction: (object) Fraction object type.
        """
        # Addition of two fractions (a/b + c/d) is calculated as (ad + cb)/bd.
        result_num = ((self.num * another_fraction.den) + (
            another_fraction.num * self.den))
        result_den = self.den * another_fraction.den
        return FractionEx02(result_num, result_den)

    def __str__(self):
        """Operator overloading for inbuilt __str__ function.

        __str__ is called by built-in print(), str() and format() functions.

        Note - The print() function works well between this class objects only.

        Returns:
          str: String in format num/den.
        """
        return str(self.num) + '/' + str(self.den)

    def __eq__(self, another_fraction):
        """Operator overloading for == operator.

        It compares two objects. If __eq__() method is not defined, python will
        use the 'is' operator for comparison.
        """
        first_num = self.num * another_fraction.den
        second_num = another_fraction.num * self.den
        return first_num == second_num


class FractionEx03(FractionEx02):
    """ Exercise 3.

    Implement the remaining simple arithmetic operators.
    (__sub__, __mul__, and __truediv__).
    """
    def __sub__(self, another_fraction):
        """Subtract Operation overloading."""

    def __mul__(self, another_fraction):
        """Multiplication operation overloading."""

    def __truediv__(self, another_fraction):
        """Truedivision operation overloading."""


class FractionEx04(FractionEx03):
    """ Exercise 4.

    Implement the remaining relational operators (__gt__, __ge__, __lt__,
    __le__, and __ne__).
    """
    def __gt__(self, another_fraction):
        """Greater than Operation overloading."""

    def __ge__(self, another_fraction):
        """Greater than or equal to operation overloading."""

    def __lt__(self, another_fraction):
        """Less than operation overloading."""

    def __le__(self, another_fraction):
        """Less than or equal to operation overloading."""

    def __ne__(self, another_fraction):
        """Not equal to operation overloading."""

"""
Exercise 6.
In the definition of fractions we assumed that negative fractions have a
negative numerator and a positive denominator. Using a negative denominator
would cause some of the relational operators to give incorrect results. In
general, this is an unnecessary constraint. Modify the constructor to allow the
user to pass a negative denominator so that all of the operators continue to
work properly.
"""

class FractionEx07(FractionEx03):
    """ Exercise 7.

    Research the __radd__ method. How does it differ from __add__? When is it
    used? Implement __radd__.
    """
    def __radd__(self, another_fraction):
        """Reverse address Operation overloading."""


class FractionEx08(FractionEx03):
    """ Exercise 8.

    Repeat the last question but this time consider the __iadd__ method.
    """
    def __iadd__(self, another_fraction):
        """Assign and add (+= eg: a += b) Operation overloading."""


class FractionEx09(FractionEx03):
    """ Exercise 9.

    Research the __repr__ method. How does it differ from __str__? When is it
    used? Implement __repr__.
    """
    def __repr__(self):
        """Official string representation overloading."""


"""
Exercise 10.
Design a class to represent a playing card. Now design a class to represent a
deck of cards. Using these two classes, implement a favorite card game.

Exercise 11.
Find a Sudoku puzzle in the local newspaper. Write a program to solve the
puzzle.
"""


if __name__ == '__main__':
    fraction_obj_01 = FractionEx02(2, 5)
    print('Fraction 01 num = ', fraction_obj_01.get_num())
    fraction_obj_02 = FractionEx02(3, 7)
    fraction_obj_03 = FractionEx02(3, 7)
    print('Fraction 02 den = ', fraction_obj_02.get_den())
    print('Addition of two fractions 2/5 and 3/7 = ',
        fraction_obj_01 + fraction_obj_02)
    print('Is fraction02 and fraction03 are equal? ',
        fraction_obj_02 == fraction_obj_03)
