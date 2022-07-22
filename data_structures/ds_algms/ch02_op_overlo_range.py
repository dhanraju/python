"""Develop our own implementation of a class that mimics built in range class.

For example, range(2, 10, 2) returned the list [2, 4, 6, 8]. However, a typical
use of the function was to support a for-loop syntax, such as for k in range(
10000000). Unfortunately, this caused the instantiation and initialization of a
list with the range of numbers. THat was an unnecessarily expensive step, in
terms of both time and memory usage.

In Python 3, this is different. Rather than creating a new list instance,
range is a class that can effectively represent the desired range of elements
without ever storing them explicitly in memory.

The biggest challenge in the implementation is properly computing the number
of elements that belong in the range, given the parameters sent by the caller
when constructing a range. By computing that value in the constructor, and
storing it as self._length, it becomes trivial to return it from the __len__
method. To properly implement a call to __getitem__(k), we simply take the
starting value of the range plus k time the step size (i.e., for k=0, we
return the start value).

We compute the number of elements in the range as
mas(0, (stop - start + step -1) // step)
It is worth testing this formula for both positive and negative step sizes.

THe __getitem__ method properly supports negative indices by converting an
index -k to len(self)-k before computing the result.
"""

class Range:
    """A class that mimic's the built-in range class."""

    def __init__(self, start, stop=None, step=1):
        """Initialize a Range instance.

        Semantics is similar to built-in range class.
        """
        if step == 0:
            raise ValueError('step value cannot be 0')

        if stop is None:            # special case of range(n)
            start, stop = 0, start  # should be treated as if range(0, n)

        # Calculate the effective lenth once.
        self._length = max(0, (stop - start + step - 1) // step)

        # need knowledge of start and step (but no stop) to support __getitem__
        self._start = start
        self._step = step

    def __len__(self):
        """Return number of entries in the range."""
        # print('** In Range.__len__ **')
        return self._length

    def __getitem__(self, k):
        """Return entry at index k (using std interpretation if negative)."""
        # print('** In Range.__getitem__ **')
        if k < 0:
            k += len(self)

        if not 0 <= k < self._length:
            raise IndexError('index out of range')

        return self._start + k * self._step


if __name__ == '__main__':
    range_var = Range(6)
    print(range_var)
    print(len(range_var))

    for i in Range(5):
        print(i)
    for j in Range(2, 10):
        print(j)
    for k in Range(0, 25, 5):
        print(k)
