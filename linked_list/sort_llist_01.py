'''Sorting linked list.'''

#pylint: disable=too-few-public-methods
class Node(object):
    '''Class contains data and link.'''
    def __init__(self):
        self.data = None
        self.link = None


class SortList(object):
    '''Sorting linked list.'''
    def __init__(self):
        self.node = Node()
        self.start = Node()
        self.visit = Node()
        self.newnode = Node()

    def read_userdata(self):
        '''Reads user input and appends it to the list.'''
        user_choice = 'y'
        while user_choice == 'y' or user_choice == 'Y':
            val = raw_input('Enter an integer value: ')
            add_atend(num)
            user_choice = raw_input('Do you want to enter new value (Y/N) or (y/n): ')

    def add_atend(self, num):
        '''Appends node at the end of list.'''
        if self.node.data is None:
            self.node.data = num
        else:
            temp = self.node
            # Traverse till the end of list.
            while temp.link is not None:
                temp = temp.link
            # Create a new node and add it to the end of list.
            new_node = Node()
            new_node.data = num
            temp.link = new_node

    def display_list(self):
        '''Display all elements present in the list.'''
        temp = self.node
        while temp.link is not None:
            print(temp.data)
            temp = temp.link
        if temp.data is not None and temp.link is None:
            print(temp.data)

    def count(self):
        '''Counts number of elements present in the list.'''
        temp = self.node
        count = 0
        while temp.link is not None:
            count += 1
            temp = temp.link
        if temp.data is not None and temp.link is None:
            count += 1
        return count

    def selection_sort_nocount_use(self):
        '''Perform selection sort technique on given linked list.'''
        # Selection sort does positional comparision. i.e., compare element at
        # 1st position with all elements till end of list and swap if required.
        # Then move on to 2nd position and perform the same. And so on...
        p = self.node
        traverse_node = self.node
        # itr_count = 0
        if self.node.data is None:
            print('No elements present in given list.')
        else:
            while p.link is not None:
                q = p.link
                while q.link is not None:
                    # Arrange list in ascending order.
                    #print('before if: p.data = ', p.data, 'q.data = ', q.data)
                    if p.data > q.data:
                        temp = p.data
                        p.data = q.data
                        q.data = temp
                        # print('inside if: p.data = ', p.data, 'q.data = ', q.data)
                    q = q.link
                    # itr_count += 1
                    # print('After %d iteration:' % itr_count)
                    # self.display_list()
                if q.data is not None and q.link is None:
                    if p.data < q.data:
                        temp = p.data
                        p.data = q.data
                        q.data = temp
                p = p.link

            # Perform bubble sort on last element.
            if p.data is not None and p.link is None:
                while traverse_node.link is not None:
                    if p.data < traverse_node.data:
                        temp = p.data
                        p.data = traverse_node.data
                        traverse_node.data = temp
                    traverse_node = traverse_node.link
                if traverse_node.data is not None and traverse_node.link is None:
                    if p.data < traverse_node.data:
                        temp = p.data
                        p.data = traverse_node.data
                        traverse_node.data = temp
                    traverse_node = traverse_node.link

    def selection_sort(self):
        '''Performs selection using count (size of list).'''
        size_of_list = self.count()
        p = self.node

        # TODO: We could modify below logic in better way.
        while p.link is not None:
            q = p.link
            # If the list contains more than two nodes.
            while q.link is not None:
                if p.data > q.data:
                    # Do Swap
                    temp = p.data
                    p.data = q.data
                    q.data = temp
                q = q.link
                # When traversal reaches last node.
                if q.link is None:
                    # Do Swap
                    temp = p.data
                    p.data = q.data
                    q.data = temp
            p = p.link

    def bubble_sort(self):
        '''Perform bubble sort technique on given linked list.'''
        # Bubble sort works by comparing each element in the list with the
        # element next to it and swapping them if required.
        p = self.node
        size_of_list = self.count()
        count = 0
        print('Number of elements in list = %d' % size_of_list)
        is_swapped = 1
        if self.node.data is None:
            print('No elements present in given list.')
        else:
            while count < size_of_list:
                p = self.node
                q = p.link
                while p.link is not None:
                    if p.data > q.data:
                        # Do swap
                        temp = p.data
                        p.data = q.data
                        q.data = temp
                        is_swapped = True
                    p = p.link
                    q = q.link
                count = count + 1



if __name__ == '__main__':
    BUBBLE_SORT_LIST = SortList()
    BUBBLE_SORT_LIST.add_atend(9)
    BUBBLE_SORT_LIST.add_atend(8)
    BUBBLE_SORT_LIST.add_atend(7)
    BUBBLE_SORT_LIST.add_atend(6)
    BUBBLE_SORT_LIST.add_atend(5)
    BUBBLE_SORT_LIST.add_atend(4)
    BUBBLE_SORT_LIST.add_atend(3)
    BUBBLE_SORT_LIST.add_atend(2)
    BUBBLE_SORT_LIST.add_atend(1)

    print('Elements BEFORE Bubble sort:')
    BUBBLE_SORT_LIST.display_list()
    BUBBLE_SORT_LIST.bubble_sort()
    print('Elements AFTER Bubble sort:')
    BUBBLE_SORT_LIST.display_list()

    SELECT_SORT_LIST = SortList()
    SELECT_SORT_LIST.add_atend(9)
    SELECT_SORT_LIST.add_atend(8)
    SELECT_SORT_LIST.add_atend(7)
    SELECT_SORT_LIST.add_atend(6)
    SELECT_SORT_LIST.add_atend(5)
    SELECT_SORT_LIST.add_atend(4)
    SELECT_SORT_LIST.add_atend(3)
    SELECT_SORT_LIST.add_atend(2)
    SELECT_SORT_LIST.add_atend(1)


    print('Elements BEFORE Selection sort:')
    SELECT_SORT_LIST.display_list()
    SELECT_SORT_LIST.selection_sort()
    print('Elements AFTER Selection sort:')
    SELECT_SORT_LIST.display_list()

    SELECT_SORT_LIST_NOCOUNT = SortList()
    SELECT_SORT_LIST_NOCOUNT.add_atend(9)
    SELECT_SORT_LIST_NOCOUNT.add_atend(8)
    SELECT_SORT_LIST_NOCOUNT.add_atend(7)
    SELECT_SORT_LIST_NOCOUNT.add_atend(6)
    SELECT_SORT_LIST_NOCOUNT.add_atend(5)
    SELECT_SORT_LIST_NOCOUNT.add_atend(4)
    SELECT_SORT_LIST_NOCOUNT.add_atend(3)
    SELECT_SORT_LIST_NOCOUNT.add_atend(2)
    SELECT_SORT_LIST_NOCOUNT.add_atend(1)


    print('Elements BEFORE Selection sort:')
    SELECT_SORT_LIST_NOCOUNT.display_list()
    SELECT_SORT_LIST_NOCOUNT.selection_sort_nocount_use()
    print('Elements AFTER Selection sort:')
    SELECT_SORT_LIST_NOCOUNT.display_list()
