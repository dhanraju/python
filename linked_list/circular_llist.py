'''Circular linked list.'''

#pylint: disable=too-few-public-methods
class Node(object):
    '''Class that contains data and link.'''
    def __init__(self):
        self.data = None
        self.link = None

class CircularLinkedList(object):
    '''Cirular Linked List operations.'''
    def __init__(self):
        self.front = Node()
        self.rear = Node()

    def addcirq_atend(self, num):
        '''Adds element at the end of queue.'''
        temp = Node()
        temp.data = num

        # If the queue is empty, create a queue with given element.
        if self.front.data is None:
            self.front = temp
        # Since queue is initialized and have some elements,
        # add new element at the end of queue.
        else:
            self.rear.link = temp

        self.rear = temp
        self.rear.link = self.front

    def delcirq_atfront(self):
        '''Deletes an element from front of queue.'''
        # If the queue is empty, nothing to do.
        if self.front.data is None:
            print('The queue is empty.')
        # Since queue has 1 or more elements, delete node at front.
        else:
            temp = Node()
            # If front and rear are pointing to same nodes,
            # it means, only one node is present in queue.
            if self.front == self.rear:
                self.front = temp
                self.rear = temp
            # If queue has more than one item, delete front item and
            # re-arrange front and rear values.
            else:
                temp = self.front
                self.front = self.front.link
                self.rear.link = self.front

    def display_list(self):
        '''Display all the elements in linked list.'''
        if self.front.data is None:
            print('No elements to display.')
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
        '''Counts number of elements present in the queue.'''
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


if __name__ == '__main__':
    CIRCULAR_LLIST = CircularLinkedList()
    CIRCULAR_LLIST.addcirq_atend(10)
    CIRCULAR_LLIST.addcirq_atend(17)
    CIRCULAR_LLIST.addcirq_atend(18)
    CIRCULAR_LLIST.addcirq_atend(5)
    CIRCULAR_LLIST.addcirq_atend(30)
    CIRCULAR_LLIST.addcirq_atend(15)

    print('Queue BEFORE deletion:')
    CIRCULAR_LLIST.display_list()

    CIRCULAR_LLIST.count()

    CIRCULAR_LLIST.delcirq_atfront()
    CIRCULAR_LLIST.delcirq_atfront()
    CIRCULAR_LLIST.delcirq_atfront()

    print('Queue AFTER deletion:')
    CIRCULAR_LLIST.display_list()
    CIRCULAR_LLIST.count()
