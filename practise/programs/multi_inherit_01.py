'''Multi inheritance example1.'''
#pylint: disable=too-few-public-methods
#pylint: disable=no-self-use
class ClassA(object):
    '''Base ClassA.'''
    def __init__(self):
        super(ClassA, self).__init__()
        print("Class A constructor.")
        self.class_a_var = 5

class ClassB(ClassA):
    '''Derived ClassB.'''
    def __init__(self):
        super(ClassB, self).__init__()
        print("Class B constructor.")
        self.class_b_var = 6

class ClassC(ClassB):
    '''Derived ClassC.'''
    def __init__(self):
        super(ClassC, self).__init__()
        print("Class C constructor.")
        self.class_c_var = 7
        self.obj_d = self.ClassD(self)
        self.obj_d.func1()

    def invoke_func2(self):
        '''Invoke function.'''
        self.obj_d.func2()

    def c_func(self):
        '''C Function.'''
        print("c func")

    class ClassD(object):
        '''Sub Class.'''
        def __init__(self, classc_obj):
            # super(ClassD, self).__init__()
            self.classc_obj = classc_obj
            self.obj_e = ClassE(self.classc_obj.class_c_var)

        def func1(self):
            '''Function 1.'''
            print("func1, c")

        def func2(self):
            '''Function 2.'''
            print("func2")
            self.classc_obj.c_func()


class ClassE(object):
    '''Base ClassE.'''
    def __init__(self, obj):
        print("ClassE")
        self.obj = obj
        print(obj)


if __name__ == '__main__':
    print("Start.")
    TEMP_OBJ = ClassC()
    print(TEMP_OBJ.class_a_var)
    print(TEMP_OBJ.class_b_var)
    print(TEMP_OBJ.class_c_var)
    TEMP_OBJ.invoke_func2()
    print("End.")

#pylint: disable=pointless-string-statement
# OUTPUT:
'''
$ python multi_inherit_01.py 
Start.
Class A constructor.
Class B constructor.
Class C constructor.
5
6
7
End.
'''
