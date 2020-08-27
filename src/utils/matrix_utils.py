from copy import deepcopy
from random import randrange, seed
import src.validators.matrix_validators as mv


def initialize(rows: int, cols: int, default_val=0) -> list:
    result = []
    if rows == 1 and cols == 1:
        return [default_val]
    elif rows != 1 and cols == 1:
        for x in range(rows):
            result.append(default_val)
    elif rows == 1 and cols != 1:
        for y in range(cols):
            result.append(default_val)
        result = [result]
    else:
        for y in range(rows):
            row = []
            for x in range(cols):
                row.append(default_val)
            result.append(row)
    return result


def functional_initialize(rows: int, cols: int, initialization_function=None, *initialization_args) -> list:
    result = []
    initialization_function = randrange if initialization_function is None else initialization_function
    args = initialization_args if len(initialization_args) > 0 else (0, 1)
    seed(5)
    if rows == 1 and cols == 1:
        return [initialization_function(*args)]
    elif rows != 1 and cols == 1:
        for x in range(rows):
            result.append(initialization_function(*args))
    elif rows == 1 and cols != 1:
        for y in range(cols):
            result.append(initialization_function(*args))
        result = [result]
    else:
        for y in range(rows):
            row = []
            for x in range(cols):
                row.append(initialization_function(*args))
            result.append(row)
    return result


def sum(*matrices: list) -> list:
    dims = mv.lengths(matrices[0])
    for matrix in matrices:
        ma_dims = mv.lengths(matrix)
        if dims[0] != ma_dims[0] or dims[1] != ma_dims[1]:
            raise Exception("Matrices' lengths do not match! \n\n"
                            + str(mv.lengths(matrix))
                            + str(mv.lengths(matrices[0]))
                            )

    result = []
    for matrix in matrices:
        if not result:
            result = deepcopy(matrix)
            continue

        # 2d matrix
        if mv.is_2d(matrix):
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    result[row][col] += matrix[row][col]
        # 1d vector
        else:
            for index in range(len(matrix)):
                result[index] += matrix[index]

    return result


def mult_core_vectors_to_scalar(matrix1: list, matrix2: list, result: list) -> list:
    for index in range(len(matrix2)):
        result[0] += matrix1[0][index] * matrix2[index]
    return result


def mult_core_vectors_to_square_matrix(matrix1: list, matrix2: list, result: list) -> list:
    for row in range(len(result)):
        for col in range(len(result[0])):
            result[row][col] = matrix1[row] * matrix2[0][col]
    return result


def mult_core_matrices(matrix1: list, matrix2: list, result: list) -> list:
    for row in range(len(matrix1)):
        for row2 in range(len(matrix2)):
            for col2 in range(len(matrix2[row2])):
                val1 = matrix1[row][row2]
                val2 = matrix2[row2][col2]
                result[row][col2] += val1 * val2
    return result


def mult_core_scalar(matrix1: list, matrix2: list) -> list:
    scalar = matrix1[0]
    result = deepcopy(matrix2)
    # 2d matrix
    if mv.is_2d(matrix2):
        for row in range(len(matrix2)):
            for col in range(len(matrix2[0])):
                result[row][col] = scalar * matrix2[row][col]
    # 1d vector
    else:
        for index in range(len(matrix2)):
            result[index] = scalar * matrix2[index]
    return result


def cofactor(mnr: float, col: float, row: float) -> float:
    return (- 1)**((col + 1) + (row + 1)) * mnr


def cofactor_adj(matrix: list, row=0, col=0) -> float:
    mat = deepcopy(matrix)
    mat.remove(mat[row])

    for rm_row in range(len(mat)):
        mat[rm_row].remove(mat[rm_row][col])

    return cofactor(determinant(mat), col, row)


def mult(matrix1: list, matrix2: list) -> list:
    dims1 = mv.lengths(matrix1)
    dims2 = mv.lengths(matrix2)

    if dims1[1] != dims2[0] and not mv.is_scalar(matrix1):
        raise Exception("Matrices' row and column does not match! \n\n"
                        + str(mv.lengths(matrix1))
                        + str(mv.lengths(matrix2))
                        )

    result = initialize(dims1[0], dims2[1])
    # vector
    if mv.is_vector(matrix1) and mv.is_line_vector(matrix2):
        return mult_core_vectors_to_square_matrix(matrix1, matrix2, result)
    elif mv.is_line_vector(matrix1) and mv.is_vector(matrix2):
        return mult_core_vectors_to_scalar(matrix1, matrix2, result)
    # scalar
    elif mv.is_scalar(matrix1):
        return mult_core_scalar(matrix1, matrix2)
    # matrix
    else:
        return mult_core_matrices(matrix1, matrix2, result)


def hadamard(*matrices):
    dims = mv.lengths(matrices[0])
    for matrix in matrices:
        if dims[0] != mv.lengths(matrix)[0] or dims[1] != mv.lengths(matrix)[1]:
            raise Exception("Matrices' lengths do not match! \n\n"
                            + str(mv.lengths(matrix))
                            + str(mv.lengths(matrices[0]))
                            )

    result = initialize(dims[0], dims[1], 1)
    for matrix in matrices:
        for row in range(len(result)):
            for col in range(len(result[row])):
                result[row][col] *= matrix[row][col]

    return result


def determinant(matrix: list, row=0) -> float:
    mv.validate_square_matrix(matrix)
    result: float = 0
    cofacs = []

    if mv.is_2d(matrix) and mv.is_scalar(matrix[0]):
        result = matrix[0][0]
    else:
        for det_col in range(len(matrix[row])):
            cofacs.append(cofactor_adj(matrix, row, det_col))

        for i in range(len(matrix[row])):
            el = matrix[row][i]
            result += el * cofacs[i]

    return result


def transpose(matrix: list) -> list:
    dims = mv.lengths(matrix)
    result = []
    # vector
    if mv.is_vector(matrix):
        result.append(matrix)
    elif mv.is_line_vector(matrix):
        return deepcopy(matrix[0])
    # matrix
    else:
        result = initialize(dims[0], dims[1])
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                result[row][col] = matrix[col][row]
    return result


def adjoint(matrix: list) -> list:
    mv.validate_square_matrix(matrix)
    dims = mv.lengths(matrix)
    result = initialize(dims[1], dims[0])

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cof = cofactor_adj(matrix, row, col)
            result[row][col] = cof

    result = transpose(result)
    return result
