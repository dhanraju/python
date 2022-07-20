from algorithms.searching import searching_algs
import unittest

class TestSearchingAlgs(unittest.TestCase):
    def setUp(self):
        self.searching_algs_obj = searching_algs.SearchingAlgs()

    def test_unordered_sequential_search_positive(self):
        testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        ret_value = self.searching_algs_obj.unorderedSequentialSearch(
            testlist, 13)
        assert(ret_value == True)

    def test_unordered_sequential_search_negative(self):
        testlist = [1, 2, 32, 8, 17, 19, 42, 13, 0]
        ret_value = self.searching_algs_obj.unorderedSequentialSearch(
            testlist, 3)
        assert(ret_value == False)

    def test_ordered_sequential_search_positive(self):
        testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
        ret_value = self.searching_algs_obj.orderedSequentialSearch(
            testlist, 13)
        assert(ret_value == True)

    def test_ordered_sequential_search_negative(self):
        testlist = [0, 1, 2, 8, 13, 17, 19, 32, 42]
        ret_value = self.searching_algs_obj.orderedSequentialSearch(
            testlist, 3)
        assert(ret_value == False)


if __name__ == '__main__':
    unittest.main()
