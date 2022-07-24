"""Arithmetic Progression."""

from data_structures.ds_algms.ch02_op_inherit_progression import Progression


class ArithmeticProgression(Progression):
    """Iterator producing an arithmetic progression."""

    def __init__(self, increment=1, start=0):
        """Creates a new arithmetic progression.

        Args:
          increment(int): The fixed constant to add to each item (default 1)
          start(int): The first term of the prgoression (default 0)
        """
        super().__init__(start)
        self._increment = increment

    def _advance(self):
        """Update current value by adding the fixed increment."""
        self._current += self._increment


if __name__ == '__main__':
    arith_prog_obj = ArithmeticProgression(2, 6)
    arith_prog_obj.print_progression(10)
    # Output: 6 8 10 12 14 16 18 20 22 24