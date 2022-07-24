"""Geometric Progression."""

from data_structures.ds_algms.ch02_op_inherit_progression import Progression


class GeometricProgression(Progression):
    """Iterator producing a geometric progression."""

    def __init__(self, base=2, start=1):
        """Create a new geometric progression.

        Args:
          base(int): The fixed constant multiplied to each term (default 2)
          start(int): The fixed term of the progression (default 1)
        """
        super().__init__(start)
        self._base = base

    def _advance(self):
        """Update current value by multipying it by the base value."""
        self._current *= self._base


if __name__ == "__main__":
    obj = GeometricProgression(4, 6)
    obj.print_progression(5)
    # Output: 6 24 96 384 1536