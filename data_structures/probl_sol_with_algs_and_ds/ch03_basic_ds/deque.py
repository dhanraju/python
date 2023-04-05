"""Deque.

A deque, also known as a double-ended queue, is an ordered collection of items
similar to the queue. It has two ends, a front and a rear, and the items remain
positioned in the collection.
New items can be added at either the front or the rear and likewise for
removing the items.
"""

class Deque:
    """The deque abstract data type."""
    def __init__(self):
        """Creates a new deque that is empty."""
        self.items = []

    def add_front(self, item):
        """Adds a new item to the front of the deque."""
        self.items.append(item)

    def add_rear(self, item):
        """Adds a new item to the rear of the deque."""
        self.items.insert(0, item)

    def remove_front(self):
        """Removes the front item from the deque.
        
        Returns the item.
        """
        return self.items.pop()

    def remove_rear(self):
        """Removes teh rear item from the deque.

        Returns the item.
        """
        return self.items.pop(0)

    def is_empty(self):
        """Checks whether the deque is empty.

        Retuns a boolen value.
        """
        return not self.items

    def size(self):
        """Returns the number of items in teh deque."""
        return len(self.items)
