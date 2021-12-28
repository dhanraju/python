'''Binary tree.'''
def binary_tree(root):
    '''Binary tree.'''
    return [root, [], []]

def insert_left(root, new_branch):
    '''Insert at left side.'''
    temp = root.pop(1) # Pop out left node of root node.
    # Insert new list into the second position of root list.
    # If the list already has something in the second position, push it down the
    # tree as the left child of the list we are adding.
    if len(temp) > 1:
        root.insert(1, [new_branch, temp, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root

def insert_right(root, new_branch):
    '''Insert at right side.'''
    temp = root.pop(2)
    if len(temp) > 1:
        root.insert(2, [new_branch, [], temp])
    else:
        root.insert(2, [new_branch, [], []])
    return root

def get_root_val(root):
    '''Get root value.'''
    return root[0]

def set_root_val(root, new_val):
    '''Set root value.'''
    root[0] = new_val

def get_right_child(root):
    '''Get right child.'''
    return root[2]

def get_left_child(root):
    '''Get left child.'''
    return root[1]


if __name__ == '__main__':
    ROOT = binary_tree(3)
    insert_left(ROOT, 4)
    insert_left(ROOT, 5)
    insert_right(ROOT, 6)
    insert_right(ROOT, 7)
    LI = get_left_child(ROOT)
    print(LI)

    # set_root_val(1, 9)
    #print(ROOT)

    #insert_left(1, 11)
    #print(root)

    print(get_right_child(get_right_child(ROOT)))
