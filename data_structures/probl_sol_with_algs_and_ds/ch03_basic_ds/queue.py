"""Queue.

A queue is an orderded collection of items where the addition of new items
happens at one end, call the rear and the removal of existing items occurs at
the other end, commonly called front. This ordering priciple is called as
FIFO, first-in-first-out.
"""

class Queue:
    """Queue Abstract Data Type implementataion."""
    def __init__(self):
        """Create an empty list."""
        self.items = []

    def enqueue(self, item):
        """Adds a new item to the rear of the queue."""
        self.items.insert(0, item)

    def dequeue(self):
        """Removes the front item from the queue.

        Returns: The list item.
        """
        return self.items.pop()

    def is_empty(self):
        """Tests to see whether the queue is empty.

        Returns: Boolean value.
        """
        return not self.items

    def size(self):
        """Returns the number of items in the queue."""
        return len(self.items)
