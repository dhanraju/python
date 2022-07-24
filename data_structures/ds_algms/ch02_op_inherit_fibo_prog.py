"""Fibonacci Progression."""
from data_structures.ds_algms.ch02_op_inherit_progression import Progression


class FibonacciProgression(Progression):
	"""Iterator producing a generalized Fibonacci progression."""

	def __init__(self, first=0, second=1):
		"""Create a new fibonacci progoression.

		Args:
		  first(int): The first term of the progression (default 0)
		  second(int): The second term of the progression (default 1)
		"""
		super().__init__(first)			# start progression at first
		self._prev = second - first		# fictitious value preceding the first

	def _advance(self):
		"""Updating current value by taking sum of previous two."""
		self._prev, self._current = self._current, self._prev + self._current


if __name__ == "__main__":
	obj = FibonacciProgression(3, 4)
	obj.print_progression(5)
	# Output: 3 4 7 11 18