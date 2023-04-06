import numpy as np

def multiply_matrices(matrix1, matrix2):

    multiply_matrix = np.dot(np.array(matrix1), np.array(matrix2))
    matrix_list = multiply_matrix.tolist()

    return matrix_list