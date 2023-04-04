"""Chapter 03 - Basic Data Structures."""


class Stack:
    """Stack is an ordered collection of items.

    The items are added to and removed from the end called 'top'. Stacks are
    ordered as LIFO - Last In First Out.
    """
    def __init__(self):
        self.items = []

    # Stack Operations.
    def is_empty(self):
        """Checks the stack is empty or not.

        Returns:
          status: (bool) True if empty; otherwise False.
        """
        return not self.items

    def size(self):
        """Returns the size of the stack."""
        return len(self.items)

    def push(self, item):
        """Pushes the item to the top of the stack."""
        self.items.insert(0, item)

    def pop(self):
        """Removes the item from the top of the stac."""
        return self.items.pop(0)

    def peek(self):
        """Returns the top item from the stack."""
        return self.items[0]

    def display(self):
        """Prints all the stack items."""
        print(self.items)
