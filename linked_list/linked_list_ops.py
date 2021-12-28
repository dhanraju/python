'''Linked list operations demonstration.'''
#pylint: disable=too-few-public-methods
class Node(object):
    '''Node class containing a data and link.'''
    def __init__(self):
        self.data = None
        self.link = None
#pylint: enable=too-few-public-methods

class LinkedList(object):
    '''Class that performs linked list operations.'''
    def __init__(self):
        self.node = Node()

    def add_atbegin(self, num):
        '''Adds a node at the beginning of a linked list.'''
        temp = Node()
        temp.data = num
        temp.link = self.node
        self.node = temp

    def add_atend(self, num):
        '''Adds a node at the end of a linked list.'''
        temp = Node()
        ref = Node()
        if self.node.data is None:
            temp.data = num
            self.node = temp
        else:
            temp = self.node
            while temp.link is not None:
                temp = temp.link
            ref.data = num
            temp.link = ref

    def add_after(self, loc, num):
        '''Adds a node after the specified number of nodes.'''
        temp = Node()
        ref = Node()
        temp = self.node
        for _ in range(loc):
            temp = temp.link
            if temp.data is None and temp.link is None:
                print('There are less than %d elements in list' % loc)
                return
        ref.link = temp.link
        ref.data = num
        temp.link = ref

    def delete(self, num):
        '''Deletes the specified node from the linked list.'''
        old = Node()
        temp = Node()
        temp = self.node
        while temp.link is not None:
            if temp.data is num:
                if temp is self.node:
                    self.node = temp.link
                else:
                    old.link = temp.link
                return
            else:
                old = temp
                temp = temp.link
        # If the element to be deleted is the last element.
        if temp.data is num and temp.link is None:
            old.link = temp.link
            return
        print('Element %d not found' % num)

    def display(self):
        '''Display the contents of the linked list.'''
        print('Contents of linked list are:')
        temp = self.node
        # print(self.node.data, self.node.link)
        while temp.link is not None:
            print(temp.data)
            temp = temp.link
        # If the list index reaches last node or list contains only one node.
        if temp.data is not None and temp.link is None:
            print(temp.data

    def count(self):
        '''Count the number of nodes present in the linked list.'''
        print('Returns count of number of nodes present in list.')
        count = 0
        temp = self.node
        while temp.link is not None:
            temp = temp.link
            count += 1
        return count + 1    # +1 is to add Last node of the list.


if __name__ == '__main__':
    L_LIST = LinkedList()
    print('Number of elements in the linked list = ', L_LIST.count())

    L_LIST.add_atend(14)
    L_LIST.add_atend(30)
    L_LIST.add_atend(25)
    L_LIST.add_atend(42)
    L_LIST.add_atend(17)

    L_LIST.display()

    L_LIST.add_atbegin(999)
    L_LIST.add_atbegin(888)
    L_LIST.add_atbegin(777)

    L_LIST.display()

    L_LIST.add_after(7, 0)
    L_LIST.add_after(2, 1)
    L_LIST.add_after(5, 99)

    L_LIST.display()
    print('Number of elements in the linked list = ', L_LIST.count())

    L_LIST.delete(99)
    L_LIST.delete(1)
    L_LIST.delete(10)
    L_LIST.delete(777)
    L_LIST.delete(0)

    L_LIST.display()
    print('Number of elements in the linked list = ', L_LIST.count())
