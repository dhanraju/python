"""Tests for Matrices."""
import matrices
import unittest
import xmlrunner


class TestMatrices(unittest.TestCase):
	MAT_A = [[1, 2, 3],
	         [1, 2, 3],
	         [1, 2, 3]]

	MAT_B = [[1, 2, 3, 4],
    	     [1, 2, 3, 4],
        	 [1, 2, 3, 4]]

	MAT_C = [[1, 2, 3, 4],
    	     [1, 2, 3, 4],
        	 [1, 2, 3, 4]]

	MAT_D = [[1, 2, 3, 4],
    	     [5, 6, 7, 8],
        	 [9, 10, 11, 12]]

	def test_is_square_matrix_01(self):
		'''Positive test case.'''
		self.assertTrue(matrices.is_square_matrix(self.MAT_A))

	def test_is_square_matrix_02(self):
		'''Negative test case.'''
		self.assertFalse(matrices.is_square_matrix(self.MAT_D))

	def test_initialize_null_matrix_01(self):
		'''Positive test case.'''
		null_matrix = []
		rows = 3
		columns = 5
		matrices.initialize_null_matrix(null_matrix, rows, columns)
		print(null_matrix)
		self.assertEqual(null_matrix,
			[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])

	def test_initialize_null_matrix_02(self):
		'''Negative test case.'''
		null_matrix = []
		rows = 3
		columns = 5
		matrices.initialize_null_matrix(null_matrix, rows, columns)
		print(null_matrix)
		self.assertNotEqual(null_matrix,
			[[1, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]])


# if __name__ == '__main__':
#	unittest.main(testRunner=xmlrunner.XMLTestRunner(output='test-reports'))

'''
TODO
if __name__ == '__main__':
    # Multiplication of two matrices.
    print '***** Matrix Multiplication. *****'
    print 'MAT_A:\n', MAT_A, '\n', 'MAT_B:\n', MAT_B, '\n'
    mul_result_mat = matrix_multiplication(MAT_A, MAT_B)
    print  'MAT_A * MAT_B:\n', mul_result_mat

    # Addition of two matrices.
    print '\n***** Matrix Addition. *****'
    print 'MAT_B:\n', MAT_B, '\n', 'MAT_C:\n', MAT_C, '\n'
    add_result_mat = matrix_addition(MAT_B, MAT_C)
    print 'MAT_B + MAT_C:\n', add_result_mat

    # Subtraction of two matrices.
    print '\n***** Matrix Subtraction. *****'
    sub_result_mat = matrix_subtraction(MAT_B, MAT_C)
    print 'MAT_B - MAT_C:\n', sub_result_mat

    # Transpose of a matrix.
    print '\n***** Transpose of a Matrix. *****'
    print 'MAT_D:\n', MAT_D, '\n'
    trans_result_mat = matrix_traspose(MAT_D)
    print 'Transpose of MAT_D is:\n', trans_result_mat

    print '\n***** Is Square Matrix. *****'
    print 'Is MAT_A a square matrix?\n', is_square_matrix(MAT_A)
    print 'Is MAT_B a square matrix?\n', is_square_matrix(MAT_B)

    print '\n***** Null Matrix. *****'
    null_matrix = []
    rows = 3
    columns = 5
    initialize_null_matrix(null_matrix, rows, columns)
    print null_matrix

    print '\n***** Identity Matrix. *****'
    identity_mat = []
    size_of_identity_mat = 4
    initialize_identity_matrix(identity_mat, size_of_identity_mat)
    print identity_mat


***** Matrix Multiplication. *****
MAT_A:
[[1, 2, 3], [1, 2, 3], [1, 2, 3]] 
MAT_B:
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]] 

MAT_A * MAT_B:
[[6, 12, 18, 24], [6, 12, 18, 24], [6, 12, 18, 24]]

***** Matrix Addition. *****
MAT_B:
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]] 
MAT_C:
[[1, 2, 3, 4], [1, 2, 3, 4], [1, 2, 3, 4]] 

MAT_B + MAT_C:
[[2, 4, 6, 8], [2, 4, 6, 8], [2, 4, 6, 8]]

***** Matrix Subtraction. *****
MAT_B - MAT_C:
[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

***** Transpose of a Matrix. *****
MAT_D:
[[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]] 

Transpose of MAT_D is:
[[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]

***** Is Square Matrix. *****
Is MAT_A a square matrix?
The given matrix is a SQUARE matrix.
True
Is MAT_B a square matrix?
The given matrix is a NOT A SQUARE matrix.
False

***** Null Matrix. *****
[[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]

***** Identity Matrix. *****
[[1, 0, 0, 0], [0, 1, 0, 0], [0, 0, 1, 0], [0, 0, 0, 1]]
'''