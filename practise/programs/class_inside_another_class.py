"""This program demonstrates class inside another class."""


class Human(object):

    # value = None

    def __init__(self, some_val):
        # self.value = 5
        self.name = 'Dhan'
        self.__class__.value = some_val
        self.head = self.Head(self.value)
        self.brain = self.Brain(self.value)
        # Declaring a class variable in instance method.
        self.__class__.value = some_val

    @classmethod
    def print_message(cls, arg_value):
        print("class value = %d" % cls.value)
        print("print(message arg_value = %d" % arg_value)

    class Head(object):
        def __init__(self, value):
            self.value = value

        def talk(self):
            return 'talking... %d' % self.value

    class Brain(object):
        def __init__(self, value):
            self.value = value

        def think(self):
            Human.print_message(10)
            return 'thinking... %d' % self.value


if __name__ == '__main__':
    dhan = Human(2)
    print(dhan.name)
    print(dhan.head.talk())
    print(dhan.brain.think())


# Ref: https://pythonspot.com/inner-classes/
'''
Notes:
The usecase is - the inner class never be used outside the definition
of the outer class.
'''