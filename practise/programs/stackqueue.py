"""This module creates stack and performs operations on it."""

class StackQueueUsingLists(object):
    """Creates stack and its operations."""
    def __init__(self):
        """Initialize empty list."""
        self.stack_list = []

    def print_stack_elements(self):
        """Prints all stack elements."""
        return self.stack_list

    def push_atend(self, element):
        """Push operation at end of list."""
        self.stack_list.append(element)

    def push_atbegin(self, element):
        """Push operation at begin of list."""
        self.stack_list.append(element)

    def pop_atend(self):
        """Pop operation."""
        self.stack_list.pop()

    def pop_atbegin(self):
        """Pop operation at begin of list."""
        if len(self.stack_list) > 0:
            self.stack_list.pop(0)
        else:
            print("Given stack is empty. Cannot perform pop operation.")

    def peek():
        """Peek operation."""
        self.stack_list[len(self.stack_list)-1]

    def size():
        """Size of stack."""
        len(self.stack_list)


def main():
    """Start of program."""
    stack_obj = StackQueueUsingLists()
    print("Enter stack elements with space between each element. eg: 1 2 3 4")
    # raw_input takes given input as string. Convert it to list using split().
    # TODO(Dhan): Implement parsing login to accept any pattery of input.
    stack_obj.stack_list = raw_input().split(" ")
    print("Current stack elements : ", stack_obj.print_stack_elements())
    # Push an element to stack.
    print("****** Stack push & pop operations ******\n")

    print("Enter an element to perform push operation.")
    # TODO(Dhan): Incomplete here.
    # stack_obj.push_atend(raw_input())
    print("------ Performing push & pop operation at end ------")
    stack_obj.pop_atend()
    print("Elements after pop at end op : ", stack_obj.print_stack_elements())
    stack_obj.pop_atbegin()
    print("Current stack elements after pop at begin op : ", stack_obj.print_stack_elements())


if __name__ == '__main__':
    main()
