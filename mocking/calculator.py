'''Calculator operation.'''
import time

#pylint: disable=too-few-public-methods
class Calculator(object):
    '''Calculator operation.'''
    def __init__(self):
        self.result = 0

    def add(self, arg1, arg2):
        '''Sum of two variables.'''
        time.sleep(10)
        self.result = arg1 + arg2
        print('%d + %d = %d' % (arg1, arg2, self.result))
        return self.result
#pylint: enable=too-few-public-methods


if __name__ == "__main__":
    OBJ = Calculator()
    print(OBJ.add(5, 6))
