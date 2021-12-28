'''Binary tree.'''
class BinaryTree(object):
    '''Binary tree.'''
    def __init__(self, root):
        self.key = root
        self.left_child = None
        self.right_child = None

    def insert_left(self, new_node):
        '''Insert at left side.'''
        if self.left_child is None:
            self.left_child = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.left_child = self.left_child
            self.left_child = tree

    def insert_right(self, new_node):
        '''Insert at right side.'''
        if self.right_child is None:
            self.right_child = BinaryTree(new_node)
        else:
            tree = BinaryTree(new_node)
            tree.right_child = self.right_child
            self.right_child = tree

    def get_right_child(self):
        '''Get right child.'''
        return self.right_child

    def get_left_child(self):
        '''Get left child.'''
        return self.left_child

    def set_root_val(self, obj):
        '''Set root value.'''
        self.key = obj

    def get_root_val(self):
        '''Get root value.'''
        return self.key

if __name__ == '__main__':
    ROOT = BinaryTree('a')
    print(ROOT.get_root_val())
    print(ROOT.get_left_child())
    ROOT.insert_left('b')
    print(ROOT.get_left_child())
    print(ROOT.get_left_child().get_root_val())
    ROOT.insert_right('c')
    print(ROOT.get_right_child()
    print(ROOT.get_right_child().get_root_val())
    ROOT.get_right_child().set_root_val('hello')
    print(ROOT.get_right_child().get_root_val())
