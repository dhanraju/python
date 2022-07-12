"""Demo's the use of operator overloading via special methods (polymporhism).

Implement a Vector class, representing the coordinates of a vector in a multi-
-dimensional space. For eg, in a 3D space, we might wish to represent a vector
with coordinates (5, -2, 3). Although it might be tempting to directly use a
Python list to represent those coordinates, a list does not provide an
appropriate abstraction for a geometric vector. In particular, if using lists,
the expression [5, -2, 3] + [1, 4, 2] results in the list [5, -2, 3, 1, 4, 2].
When working with vectors, if u = (5, -2, 3) and v = (1, 4, 2), one would expect
the expression u + v, to return a 3D vector with coordinates (6, 2, 5)."""


class Vector:
  """Represent a vector in a multidimensional space."""

  def __init__(self, d):
    """Create d-dimensional vector of zeros."""
    self._coords = []
    self._coords = [0] * d

  def __len__(self):  # operator overloading.
    """Return the dimension of the vector."""
    return len(self.__coords)

  def __getitem__(self):
    """Return jth coordinate of vector."""
    return self._coords[j]

  def __setitem__(self, j, val):
    """Set jth coordinate of vector to a given value."""
    print('*** j = %d, val = %d' % (j, val))
    self.__coords[j] = val

  def __add__(self, other):
    """Returns sum of two vectors."""
    print('*** Add vectors ***')
    if len(self) != len(other):  # relies on existing __len__ method
      raise ValueError('dimensions must agree')
    result = Vector(len(self))
    for j in range(len(self)):
      # Supports polymorphism that operates on multi dimensional vector.
      result[j] = self[j] + other[j]
    return result

  def __eq__(self, other):
    """Return True if vector has some coordinates as other."""
    return self._coords == other.__coords

  def __ne__(self, other):
    """Return True if vector differs from other."""
    return not self == other  # rely on existing __eq__ defintion

  def __str__(self):
    """Produce string representation of vector."""
    return '<' + str(self._coords)[1:-1] + '>'  # adapt list representation


if __name__ == '__main__':
  vector_dimension = 3
  vector_a = Vector(vector_dimension)
  vector_b = Vector(vector_dimension)
  print('*** vector_a = ', vector_a)
  j = 0
  vector_a[0] = 5
  vector_a[1] = -2
  vector_a[2] = 3
  vector_b[0] = 1
  vector_b[1] = 4
  vector_b[2] = 2
  print('*** vector_a + vector_b = ', vector_a + vector_b)
  # for val in (5, -2, 3):
  #  vector_a.__setitem__(j, val)
  #  j += 1
  # print('Values of Vector a = ', vector_a)
    
  # k = 0
  # for val in (1, 4, 2):
  #   vector_a.__setitem__(k, val)
  #  k += 1
  # print('Values of Vector b = ', vector_b)
