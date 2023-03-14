'''Matrices Demonstration using lists.'''

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


def initialize_null_matrix(mat, rows, columns):
    '''Initialize Matrix with all zeros.'''
    for i in range(rows):
        each_row = []
        for j in range(columns):
            each_row.append(0)
        mat.append(each_row)
    # return mat

def num_of_rows_columns(mat):
    '''Returns number of rows of columns of a matrix.'''
    rows = len(mat)
    if rows > 0:
        columns = len(mat[0])
    return (rows, columns)

def is_square_matrix(mat):
    '''Identifies the given matrix is a square matrix or not.'''
    rows, columns = num_of_rows_columns(mat)
    if rows is columns:
        # print('The given matrix is a SQUARE matrix.')
        return True
    else:
        # print('The given matrix is a NOT A SQUARE matrix.')
        return False

def initialize_identity_matrix(mat, size):
    '''Initialize an identity Matrix for a given size of matrix.'''
    rows = size
    columns = size
    for i in range(rows):
        each_row = []
        for j in range(columns):
            if i is j:
                each_row.append(1)
            else:
                each_row.append(0)
        mat.append(each_row)

def matrix_multiplication(mat_a, mat_b):
    '''Performs multiplication on two matrices.'''
    rows_a, columns_a = num_of_rows_columns(mat_a)
    rows_b, columns_b = num_of_rows_columns(mat_b)
    result_mat = []
    if columns_a is rows_b:
        # Initialize resultant matrix with
        # rows = rows of a and columns = columns of b.
        initialize_null_matrix(result_mat, rows_a, columns_b)
        # print(result_mat
        for k in range(rows_a):
            for i in range(columns_b):
                for j in range(columns_a):
                    result_mat[k][i] += mat_a[k][j] * mat_b[j][i]
        return result_mat
    else:
        print('Multiplication not possible: Invalid sizes of matrices.')

def matrix_addition(mat_a, mat_b):
    '''Performs addition on two matrices.'''
    rows_a, columns_a = num_of_rows_columns(mat_a)
    rows_b, columns_b = num_of_rows_columns(mat_b)
    result_mat = []
    if rows_a is rows_b and columns_a is columns_b:
        initialize_null_matrix(result_mat, rows_a, columns_a)
        for i in range(rows_a):
            for j in range(columns_a):
                result_mat[i][j] = mat_a[i][j] + mat_b[i][j]
        return result_mat
    else:
        print('Addition not possible: Invalid sizes of matrices.')

def matrix_subtraction(mat_a, mat_b):
    '''Performs subtraction on two matrices.'''
    rows_a, columns_a = num_of_rows_columns(mat_a)
    rows_b, columns_b = num_of_rows_columns(mat_b)
    result_mat = []
    if rows_a is rows_b and columns_a is columns_b:
        initialize_null_matrix(result_mat, rows_a, columns_a)
        for i in range(rows_a):
            for j in range(columns_a):
                result_mat[i][j] = mat_a[i][j] - mat_b[i][j]
        return result_mat
    else:
        print('Subtraction not possible: Invalid sizes of matrices.')

def matrix_traspose(mat):
    '''Performs transpose of a matrix.'''
    rows, columns = num_of_rows_columns(mat)
    result_mat = []
    initialize_null_matrix(result_mat, columns, rows)
    for i in range(rows):
        for j in range(columns):
            result_mat[j][i] = mat[i][j]
    return result_mat


if __name__ == '__main__':
    # Multiplication of two matrices.
    # print('***** Matrix Multiplication. *****')
    # print('MAT_A:\n', MAT_A, '\n', 'MAT_B:\n', MAT_B, '\n')
    mul_result_mat = matrix_multiplication(MAT_A, MAT_B)
    # print( 'MAT_A * MAT_B:\n', mul_result_mat)

    # Addition of two matrices.
    # print('\n***** Matrix Addition. *****')
    # print('MAT_B:\n', MAT_B, '\n', 'MAT_C:\n', MAT_C, '\n')
    add_result_mat = matrix_addition(MAT_B, MAT_C)
    # print('MAT_B + MAT_C:\n', add_result_mat)

    # Subtraction of two matrices.
    # print('\n***** Matrix Subtraction. *****')
    sub_result_mat = matrix_subtraction(MAT_B, MAT_C)
    # print('MAT_B - MAT_C:\n', sub_result_mat)

    # Transpose of a matrix.
    # print('\n***** Transpose of a Matrix. *****')
    # print('MAT_D:\n', MAT_D, '\n')
    trans_result_mat = matrix_traspose(MAT_D)
    # print('Transpose of MAT_D is:\n', trans_result_mat)

    # print('\n***** Is Square Matrix. *****')
    # print('Is MAT_A a square matrix?\n', is_square_matrix(MAT_A))
    # print('Is MAT_B a square matrix?\n', is_square_matrix(MAT_B))

    # print('\n***** Null Matrix. *****')
    null_matrix = []
    rows = 3
    columns = 5
    initialize_null_matrix(null_matrix, rows, columns)
    # print(null_matrix)

    # print('\n***** Identity Matrix. *****')
    identity_mat = []
    size_of_identity_mat = 4
    initialize_identity_matrix(identity_mat, size_of_identity_mat)
    # print(identity_mat)