'''Linked list operations demonstration.'''
#pylint: disable=too-few-public-methods
class Node(object):
    '''Node class containing a data and link.'''
    def __init__(self):
        self.data = None
        self.link = None
#pylint: enable=too-few-public-methods


class AscendOrderLList(object):
    '''Class that performs ascending order on linked list.'''
    def __init__(self):
        self.node = Node()

    def add_node(self, num):
        '''Adds node to an ascending order linked list.'''
        temp = self.node
        new_node = Node()
        new_node.data = num
        # If list is empty or if new node is to be insterted at the first node.
        if temp.data is None or temp.data > num:
            self.node = new_node
            self.node.link = temp
        else:
            # Traverse the entire linked list to search the position to insert
            # new node.
            while temp.link is not None and temp.data <= num:
                temp_backup = temp
                temp = temp.link
            temp_backup.link = new_node
            new_node.link = temp

    def display(self):
        '''Display contents of the linked list.'''
        temp = self.node
        while temp.link is not None:
            print(temp.data)
            temp = temp.link
        # If the list index reaches last node or list contains only one node.
        if temp.data is not None and temp.link is None:
            print(temp.data)

    def count(self):
        '''Counts the number of nodes present in the linked list.'''
        count = 0
        temp = self.node
        while temp.link is not None: # or temp.data is not None:
            count += 1
            temp = temp.link
        return count


if __name__ == '__main__':
    ASC_ORDER_LLIST = AscendOrderLList()

    ASC_ORDER_LLIST.add_node(5)
    ASC_ORDER_LLIST.add_node(1)
    ASC_ORDER_LLIST.add_node(6)
    ASC_ORDER_LLIST.add_node(4)
    ASC_ORDER_LLIST.add_node(7)
    ASC_ORDER_LLIST.add_node(8)
    ASC_ORDER_LLIST.add_node(2)

    ASC_ORDER_LLIST.display()

    print('Number of elements in the linked list = %d' % ASC_ORDER_LLIST.count()
