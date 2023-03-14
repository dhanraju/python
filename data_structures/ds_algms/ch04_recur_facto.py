"""Implement the factorial function using recursion."""

class Factorial:
	"""Factorial function."""

	def get_factorial(self, n):
		"""Returns the factorial a given number."""
		if n == 0:
			return 1
		else:
			return n * self.get_factorial(n - 1)


if __name__ == "__main__":
	facto_obj = Factorial()
	print(facto_obj.get_factorial(3))
	print(facto_obj.get_factorial(4))