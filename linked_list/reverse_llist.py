'''Reversing a linked list.'''

#pylint: disable=too-few-public-methods
class Node(object):
    '''Node class contains data and link.'''
    def __init__(self):
        self.data = None
        self.link = None

class LList(object):
    '''Class that performs operations on linked list.'''
    def __init__(self):
        self.node = Node()

    def add_atbegin(self, num):
        '''Add element at the beginning of list.'''
        temp = Node()
        temp.data = num
        temp.link = self.node
        self.node = temp

    def reverse(self):
        '''Reverse given linked list.'''
        list_traveller = self.node
        temp = Node()
        starting_node = Node()

        while list_traveller.link is not None:
            starting_node = temp
            temp = list_traveller
            list_traveller = list_traveller.link
            temp.link = starting_node
        self.node = temp

    def display(self):
        '''Displays the contents of linked list.'''
        temp = self.node
        while temp.link is not None:
            print(temp.data)
            temp = temp.link

    def count(self):
        '''Counts number of nodes present in the linked list.'''
        count = 0
        temp = self.node

        while temp.link is not None:
            count += 1
            temp = temp.link
        return count


if __name__ == '__main__':
    LLIST = LList()

    LLIST.add_atbegin(7)
    LLIST.add_atbegin(43)
    LLIST.add_atbegin(17)
    LLIST.add_atbegin(3)
    LLIST.add_atbegin(23)
    LLIST.add_atbegin(5)

    LLIST.display()

    print('Number of elements in the linked list = %d' % LLIST.count())