'''Merging of two linked list with a condition of removing duplicates.'''

#pylint: disable=too-few-public-methods
class Node(object):
    '''Class contains data and link.'''
    def __init__(self):
        self.data = None
        self.link = None

class AscendOrderLList(object):
    '''Linked list class.'''
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
        # print('in display: ', temp.data)
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
        if temp.data is not None and temp.link is None:
            count += 1
        return count

    def merge(self, llist1, llist2):
        '''Merge two linked lists, restricting common elements to occur only
        one in the final list.'''
        # If both lists are empty.
        if llist1.link is None and llist2.link is None:
            return

        # Traverse both linked lists till the end. If end of any one list is
        # reached, loop is terminated.
        while llist1.link is not None and llist2.link is not None:
            new_node = Node()
            if llist1.data < llist2.data:
                new_node.data = llist1.data
                llist1 = llist1.link
            else:
                if llist2.data < llist1.data:
                    new_node.data = llist2.data
                    llist2 = llist2.link
                else:
                    if llist1.data == llist2.data:
                        new_node.data = llist2.data
                        llist1 = llist1.link
                        llist2 = llist2.link
            if self.node.data is None:
                traverse_node = Node()
                traverse_node.data = new_node.data
                self.node = traverse_node
            else:
                traverse_node = Node()
                traverse_node = self.node
                while traverse_node.link is not None:
                    traverse_node = traverse_node.link
                traverse_node.link = new_node

        # If end of first list has not been reached.
        while llist1.link is not None:
            traverse_node = Node()
            new_node = Node()
            traverse_node = self.node
            new_node.data = llist1.data
            while traverse_node.link is not None:
                traverse_node = traverse_node.link
            traverse_node.link = new_node
            llist1 = llist1.link

        # If end of second list has not been reached.
        while llist2.link is not None:
            traverse_node = Node()
            new_node = Node()
            traverse_node = self.node
            new_node.data = llist2.data
            while traverse_node.link is not None:
                traverse_node = traverse_node.link
            traverse_node.link = new_node
            llist2 = llist2.link


if __name__ == '__main__':
    ASC_ORDER_LLIST_1 = AscendOrderLList()
    ASC_ORDER_LLIST_2 = AscendOrderLList()
    ASC_ORDER_LLIST_3 = AscendOrderLList()

    ASC_ORDER_LLIST_1.add_node(9)
    ASC_ORDER_LLIST_1.add_node(12)
    ASC_ORDER_LLIST_1.add_node(14)
    ASC_ORDER_LLIST_1.add_node(17)
    ASC_ORDER_LLIST_1.add_node(35)
    ASC_ORDER_LLIST_1.add_node(61)
    ASC_ORDER_LLIST_1.add_node(79)

    print('First linked list.')
    ASC_ORDER_LLIST_1.display()
    print('No. of elements in the 1st llist = %d' % ASC_ORDER_LLIST_1.count())

    ASC_ORDER_LLIST_2.add_node(12)
    ASC_ORDER_LLIST_2.add_node(17)
    ASC_ORDER_LLIST_2.add_node(24)
    ASC_ORDER_LLIST_2.add_node(36)
    ASC_ORDER_LLIST_2.add_node(59)
    ASC_ORDER_LLIST_2.add_node(64)
    ASC_ORDER_LLIST_2.add_node(87)

    print('Second linked list.')
    ASC_ORDER_LLIST_2.display()
    print('No. of elements in the 2nd llist = %d' % ASC_ORDER_LLIST_2.count())

    ASC_ORDER_LLIST_3.merge(ASC_ORDER_LLIST_1.node, ASC_ORDER_LLIST_2.node)
    print('Merged list is:')
    ASC_ORDER_LLIST_3.display()
    print('No. of elements in the 3rd llist = %d' % ASC_ORDER_LLIST_3.count())
