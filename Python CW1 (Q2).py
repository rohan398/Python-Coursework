# STUDENT NUMBER : 22031444
import numpy as np
from numpy.linalg import LinAlgError


def matrix_multiplication(*argv):
    """
    Perform matrix multiplication for the given matrices.

    :param argv: Matrices passed as optional args
    :return: Matrix obtained after multiplication of given matrices
    """
    matrix_1 = argv[0]
    matrix_2 = argv[1]
    
    # Matrix multiplication is possible only if 1st matrix columns size is equal to second matrix row size
    matrix_1_columns_size = matrix_1.shape[1]
    matrix_2_rows_size = matrix_2.shape[0]
    
    if matrix_1_columns_size == matrix_2_rows_size:
        # Initialise output matrix of size m*n with 0s.
        output = np.zeros((matrix_1.shape[0], matrix_2.shape[1]))
        for i in range(len(matrix_1)):
            for j in range(matrix_2.shape[1]):
                for k in range(len(matrix_2)):
                    output[i][j] = output[i][j] + (matrix_1[i][k] * matrix_2[k][j])
    else:
        print("Matrix dimension mismatch")
        return None

    print("Multiplication is successful")
    return output


def linear_solver(matrix, column_vector):
    """

    :param matrix:
    :param column_vector:
    :return:
    """
    try:
        # Perform the matrix multiplication on inverse of first matrix and column vector
        res = matrix_multiplication(np.linalg.inv(matrix), column_vector)
    except LinAlgError:
        print("The Inputs are not suitable for a linear system of equations.")
        return None
    print("Unique Solution!")
    return res


def LLS(A, b):
    """
    Perform Linear Least squares method on given matrices.
    :param A:
    :param b:
    :return:
    """
    # Get Transpose of Matrix A
    a_transpose = np.transpose(A)
    # Get the Moore–Penrose inverse of matrix A.
    moore_penrose_inverse = matrix_multiplication(np.linalg.inv(matrix_multiplication(a_transpose, A)), a_transpose)

    return matrix_multiplication(moore_penrose_inverse, b)


