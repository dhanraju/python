'''Multi inheritance example.'''
#pylint: disable=too-few-public-methods
class ClassA(object):
    '''Base ClassA.'''
    def __init__(self):
        super(ClassA, self).__init__()
        print("Class A constructor.")

class ClassB(object):
    '''Base ClassB.'''
    def __init__(self):
        super(ClassB, self).__init__()
        print("Class B constructor.")

class Trial1(ClassA, ClassB):
    '''Dervied class Trial1.'''
    def __init__(self):
        super(Trial1, self).__init__()
        print("triail1 constructor.")

if __name__ == '__main__':
    print("Start.")
    Trial1()
    print("End.")


# Output:
# $ python multi_inherit.py
# Start.
# Class B constructor.
# Class A constructor.
# triail1 constructor.
# End.

# NOTES:
# super() function handles inconsistent order of class hierarchy in multiple
# inheritance cases. Python uses "method resolution order" (MRO) algorithm in
# context of complete inheritance hierarchy inorder to resolve __init__ is
# calculated using "depth-first left-to-right traversal". super(ClassName,
# self).__init__() provides next __init__ method dictated by MRO.

# Refs:
# http://stackoverflow.com/questions/3277367/how-does-pythons-super-work-with-multiple-inheritance
# https://learnpythonthehardway.org/book/ex44.html
