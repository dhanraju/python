"""This module demonstrates single linked list."""

#pylint: disable=too-few-public-methods
class Node(object):
    '''Node contains data and next.'''
    def __init__(self):
        self.data = None
        self.next = None

class LinkedList(object):
    '''Linked list demo.'''
    def __init__(self):
        self.cur_node = None

    def add_node_atbegin(self, data):
        '''Add node at beginning of list.'''
        new_node = Node()
        new_node.data = data
        new_node.next = self.cur_node
        self.cur_node = new_node

    def print_linkedlist(self):
        '''Print elements in linked list.'''
        node = self.cur_node
        while node:
            print(node.data)
            node = node.next


L_LIST = LinkedList()
L_LIST.add_node_atbegin(1)
L_LIST.add_node_atbegin(2)
L_LIST.add_node_atbegin(3)

L_LIST.print_linkedlist()
