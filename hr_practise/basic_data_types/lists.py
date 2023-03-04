"""List operations.

Consider a list (list = []). You can perform the following commands:

1. insert i e: Insert integer e at position i.
2. print: Print the list.
3. remove e: Delete the first occurrence of integer e.
4. append e: Insert integer e at the end of the list.
5. sort: Sort the list.
6. pop: Pop the last element from the list.
7. reverse: Reverse the list.
Initialize your list and read in the value of n followed by n lines of commands
where each command will be of the 7 types listed above. Iterate through each
command in order and perform the corresponding operation on your list.
"""

LIST_OPERATIONS = {
    1 : 'insert',
    2 : 'print',
    3 : 'remove',
    4 : 'append',
    5 : 'sort',
    6 : 'pop',
    7 : 'reverse',
}

LIST_OPERATIONS = {
    1 : 'insert',
    2 : 'print',
    3 : 'remove',
    4 : 'append',
    5 : 'sort',
    6 : 'pop',
    7 : 'reverse',
}

def list_ops(number_of_list_commands):
    """Perform list operations."""
    given_list = []
    for _ in range(number_of_list_commands):
        given_input = input().strip().split()
        list_op = given_input[0]
        if list_op == LIST_OPERATIONS[1]:
            # Insert operation
            # Enter the position of list index
            i = int(given_input[1])
            # Enter an int value to insert into the list
            e = int(given_input[2])
            if len(given_list) == i or i > len(given_list):
                # If he given position is greater than the len of list.
                # So appending at the end of the list.``
                given_list.append(e)
            else:
                given_list.insert(i, e)
        elif list_op == LIST_OPERATIONS[2]:
            # Print operation
            print(given_list)
        elif list_op == LIST_OPERATIONS[3]:
            # Remove operation
            # Enter the given value in the list for the removal.
            e = int(given_input[1])
            given_list.remove(e)
        elif list_op == LIST_OPERATIONS[4]:
            # Append operation
            # Enter an int value to append at the last position of list.
            e = int(given_input[1])
            given_list.append(e)
        elif list_op == LIST_OPERATIONS[5]:
            # Sort operation
            given_list.sort()
        elif list_op == LIST_OPERATIONS[6]:
            # Pop operation
            given_list.pop()
        elif list_op == LIST_OPERATIONS[7]:
            # Reverse operation
            given_list.reverse()
    return given_list

if __name__ == '__main__':
    N = int(input())
    list_ops(N)


'''
Input (stdin):
12
insert 0 5
insert 1 10
insert 0 6
print
remove 6
append 9
append 1
sort
print
pop
reverse
print

Expected Output (stdout):
[6, 5, 10]
[1, 5, 9, 10]
[9, 5, 1]
'''