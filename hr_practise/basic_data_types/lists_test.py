from hr_practise.basic_data_types import lists
import unittest


class TestListOps(unittest.TestCase):
    """Unit test for lists problem."""
    def setUp(self):
        pass
    
    def test_insert(self):
        num_of_commands = 1
        print(lists.list_ops(num_of_commands))
        # assert [5] == lists.list_ops(2)


if __name__ == '__main__':
    unittest.main()