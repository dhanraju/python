"""Lists.

A list is a collection of items where each item holds a relative position with
respect to the others. The type of list is an unordered list.
"""

class Node:
    """The node is the building block of the linked list implementation.

    Each node object must hold at least two pieces of information. The data
    field and a reference to the next node. To construct a node, we need to
    supply the initial data value for the node.
    """
    def __init__(self, init_data):
        """Initialize node object with initial data."""
        self.data = init_data
        self.next = None

    def get_data(self):
        """Returns the data from the node."""
        return self.data

    def get_next(self):
        """Returns the reference of the node."""
        return self.next

    def set_data(self, new_data):
        """Sets new data of the node."""
        self.data = new_data

    def set_next(self, new_next):
        """Sets new reference of the node."""
        self.next = new_next


class UnorderedList:
    """The unordered list abstract data type.
    
    The unordered list will be built from a collection of nodes, each linked to
    the next by explicit references.
    """
    def __init__(self):
        """Creates only head reference for the unordered list."""
        self.head = None

    def is_empty(self):
        """Check the head reference is None."""
        return self.head is None

    def add(self, item):
        """Creates a new node with the item.
        
        And adds it at the begining of the list.
        """
        temp = Node(item)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        """Returns the size of the list by travesing the list."""
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item):
        """Searches for the item in the list."""
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() is item:
                found = True
            else:
                current = current.get_next()
        return found

    def remove(self, item):
        """Removes the item from the list."""
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() is item:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.set_next(current.get_next())
