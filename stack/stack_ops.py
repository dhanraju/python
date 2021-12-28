'''Stack operations demonstration.'''
#pylint: disable=too-few-public-methods
class Node(object):
    '''Node class containing a data and link.'''
    def __init__(self):
        self.data = None
        self.link = None
#pylint: enable=too-few-public-methods

class Stack(object):
    '''Stack operations.'''
    def __init__(self):
        self.top = Node()

    def push(self, val):
        '''Push value at the top of stack also called as add node at beginning.'''
        temp = Node()
        temp.data = val
        temp.link = self.top
        self.top = temp

    def pop(self):
        '''Pop value at the top of stack also called as delete node at beginning.'''
        if self.top.data is None:
            print("Stack is empty")
            return
        temp = Node()
        temp = self.top
        print("Value popped = ", self.top.data)
        self.top = self.top.link

    def display(self):
        '''print stack elements.'''
        temp = self.top
        if temp.data is None:
            print("Stack is empty. No elements to display.")
            return
        while temp.data is not None:
            print(temp.data)
            temp = temp.link


if __name__ == '__main__':
    STACK_OBJ = Stack()
    STACK_OBJ.push(14)
    STACK_OBJ.push(-3)
    STACK_OBJ.push(18)
    STACK_OBJ.push(29)
    STACK_OBJ.push(31)
    STACK_OBJ.push(16)

    STACK_OBJ.display()

    STACK_OBJ.pop()
    STACK_OBJ.pop()

    print("After popping.")
    STACK_OBJ.display()
    STACK_OBJ.pop()
    STACK_OBJ.pop()
    STACK_OBJ.pop()
    STACK_OBJ.pop()
    STACK_OBJ.pop()