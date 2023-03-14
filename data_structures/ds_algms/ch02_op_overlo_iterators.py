"""Iterators and Iterables.

An iterator is an object that manages an iteration through a series of values.
If variable i identifies an iterator object, then each call to the built-in
function next(i) produces a subsequent element from the underlying series, with
a StopIteration exception raised to indicate that there are no further
elements.

An iterable is an object 'obj' that produces an iterator via syntax iter(obj).
Eg: Basic container types, such as list, tuple and set qualify as iterable
types. Furthermore, a string can produce an iteration of its characters, a
dictionary can produce an iteration of its keys, and a file can produce an
iteration of its lines.
"""


class SequenceIterator:
    """An iterator for any of Python's sequence types."""

    def __init__(self, sequence):
        """Create an iterator for the given sequence."""
        self._seq = sequence  # Copy of the given data.
        # Reference to the underlying data, will increment to 0 on first call
        # to next element.
        self._k = -1

    def __next__(self):
        """Return the next element, or else raie StopIteration error."""
        self._k += 1
        if self._k < len(self._seq):
            return(self._seq[self._k])
        else:
            # print('*** End of iteration. ***')
            raise StopIteration()

    def __iter__(self):
        """By convention, an iterator must return itself as an iterator."""
        # print('*** In iter ***')
        return self


if __name__ == "__main__":
    list_obj = [11, 12, 13, 14, 15]
    seq_itr = SequenceIterator(list_obj)
    for i in seq_itr:
        print('*** i = %d' % i)