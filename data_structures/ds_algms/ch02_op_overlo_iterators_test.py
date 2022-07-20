import unittest
from data_structures.ds_algms.ch02_op_overlo_iterators import SequenceIterator

class TestSequenceIterator(unittest.TestCase):
    def setUp(self):
        self.seq_var = [11, 12, 13, 14, 15]
        self.seq_itr_obj = SequenceIterator(self.seq_var)

    def test_seq_init(self):
        seq_itr = self.seq_itr_obj
        assert type(seq_itr) == type(SequenceIterator(self.seq_var))

    def test_seq_next(self):
        seq_itr = self.seq_itr_obj
        assert seq_itr.__next__() in self.seq_var

    def test_seq_iter(self):
        seq_itr = self.seq_itr_obj
        result_seq = []
        for val in seq_itr:
            result_seq.append(val)
        assert result_seq == self.seq_var


if __name__ == "__main__":
  unittest.main()