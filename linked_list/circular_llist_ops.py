'''Operations on Circular linked lists.'''

#pylint: disable=too-few-public-methods
class Node(object):
    '''Class contains data and link.'''
    def __init__(self):
        self.data = None
        self.link = None


class CircularLListOps(object):
    '''Circular linked list operations.'''
    def __init__(self):
        self.front = Node()
        self.rear = Node()

    def addcirq_atend(self, num):
        '''Adds node at the end of circular queue.'''
        temp = Node()
        temp.data = num
        # If the list is empty, create first node.
        if self.front.data is None:
            self.front = temp
        else:
            self.rear.link = temp

        self.rear = temp
        self.rear.link = self.front

    def concat(self, first_list, second_list):
        '''Concatenates two linked lists.'''
        temp = Node()
        # If the first list is empty.
        '''if first_list.data is None:
            first_list = second_list
        else:
            # If the second list is empty.
            if second_list.data is not None:
                temp = first_list
                while temp.link is not None:
                    print('lock')
                    temp = temp.link
                temp.link = second_list'''

    def display(self):
        '''Displays contents of the linked list.'''
        if self.front.data is None:
            print('The queue is empty.')
        else:
            # print('Elements present in linked list:')
            temp = self.front
            while temp.link is not self.front:
                print(temp.data)
                temp = temp.link
            # print(last element in the queue.
            if temp.link is self.front:
                print(temp.data)

    def count(self):
        '''Counts the number of nodes present in the lined list.'''
        count = 0
        if self.front.data is None:
            print('No of elements present in the queue to count')
        else:
            temp = self.front
            while temp.link is not self.front:
                count += 1
                temp = temp.link
            # Count last element.
            if temp.link is self.front:
                count += 1
        print('Number of elements present in the queue: %d' % count)

    def erase(self):
        '''Erases all nodes from a linked list.'''
        print('erase')
        temp = Node()

        while self.front is not None:
            temp = self.front
            temp.link = None
            self.front = self.front.link
            temp = Node()


if __name__ == '__main__':
    CIRCULAR_LLIST_OPS_FIRST = CircularLListOps()
    CIRCULAR_LLIST_OPS_SECOND = CircularLListOps()

    CIRCULAR_LLIST_OPS_FIRST.addcirq_atend(1)
    CIRCULAR_LLIST_OPS_FIRST.addcirq_atend(2)
    CIRCULAR_LLIST_OPS_FIRST.addcirq_atend(3)
    CIRCULAR_LLIST_OPS_FIRST.addcirq_atend(4)

    print('First List:')
    CIRCULAR_LLIST_OPS_FIRST.display()

    CIRCULAR_LLIST_OPS_FIRST.count()

    CIRCULAR_LLIST_OPS_SECOND.addcirq_atend(5)
    CIRCULAR_LLIST_OPS_SECOND.addcirq_atend(6)
    CIRCULAR_LLIST_OPS_SECOND.addcirq_atend(7)
    CIRCULAR_LLIST_OPS_SECOND.addcirq_atend(8)

    print('Second List:')
    CIRCULAR_LLIST_OPS_SECOND.display()

    CIRCULAR_LLIST_OPS_SECOND.count()

    # CIRCULAR_LLIST_OPS_FIRST.concat(CIRCULAR_LLIST_OPS_FIRST.front, CIRCULAR_LLIST_OPS_SECOND.front)
    # CIRCULAR_LLIST_OPS_FIRST.display()

    CIRCULAR_LLIST_OPS_FIRST.erase()
    print('Number of elements after erasing:')
    # CIRCULAR_LLIST_OPS_FIRST.display()