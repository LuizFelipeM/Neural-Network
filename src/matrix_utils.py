from copy import deepcopy


def initialize(y_dim, x_dim, default_val = 0):
    if y_dim == 1 and x_dim == 1:
        return default_val

    result = []
    for y in range(y_dim):
        row = []
        for x in range(x_dim):
            row.append(default_val)
        result.append(row)
    return result


def lengths(matrix):
    x_dim = len(matrix)
    y_dim = len(matrix[0]) if isinstance(matrix[0], list) else 1
    return (x_dim, y_dim)


def sum(*matrices):
    dims = lengths(matrices[0])
    for matrix in matrices:
        if dims[0] != lengths(matrix)[0] or dims[1] != lengths(matrix)[1]:
            raise Exception("Matrices' lengths do not match! \n\n"
                            + str(lengths(matrix))
                            + str(lengths(matrices[0]))
                            )

    result = []
    for matrix in matrices:
        if not result:
            result = deepcopy(matrix)
            continue

        # 2d matrix
        if isinstance(matrix[0], list):
            for row in range(len(matrix)):
                for col in range(len(matrix[0])):
                    result[row][col] += matrix[row][col]
        # 1d vector
        else:
            for index in range(len(matrix)):
                result[index] += matrix[index]

    return result


def mult(matrix1: list, matrix2: list):
    dims1 = lengths(matrix1)
    dims2 = lengths(matrix2)

    if dims1[1] != dims2[0]:
        raise Exception("Matrices' row and column does not match! \n\n"
                        + str(lengths(matrix1))
                        + str(lengths(matrix2))
                        )

    # vector
        # escalar
    if dims1[1] == 1 and dims2[0] == 1:
        result = initialize(dims1[0], dims2[1])
        for row in range(len(result)):
            for col in range(len(result[0])):
                result[row][col] = matrix1[row] * matrix2[0][col]
        # square matrix
    elif dims1[0] == 1 and dims2[1] == 1:
        result = 0
        for index in range(len(matrix2)):
            result += matrix1[0][index] * matrix2[index]
        return result
    # matrix
    else:
        result = initialize(dims1[0], dims2[1])
        for row in range(len(matrix1)):
            for row2 in range(len(matrix2)):
                for col2 in range(len(matrix2[row2])):
                    val1 = matrix1[row][row2]
                    val2 = matrix2[row2][col2]
                    result[row][col2] += val1 * val2

    return result


def cofactor(mnr: float, col: float, row: float) -> float:
    return (- 1)**((col + 1) + (row + 1)) * mnr


def cofactor_adj(matrix: list, row=0, col=0) -> float:
    mat = deepcopy(matrix)
    mat.remove(mat[row])

    for rm_row in range(len(mat)):
        mat[rm_row].remove(mat[rm_row][col])

    return cofactor(determinant(mat), col, row)


def determinant(matrix: list, row=0) -> float:
    result: float = 0
    cofacs: list = []
    dims = lengths(matrix)

    if dims[0] != dims[1]:
        raise Exception("Matrix must have the same number of columns and rows")

    if dims[0] == 1 and dims[1] == 1:
        result = matrix[0][0]
    else:
        for det_col in range(len(matrix[row])):
            cofacs.append(cofactor_adj(matrix, row, det_col))

        for i in range(len(matrix[row])):
            el = matrix[row][i]
            result += el * cofacs[i]

    return result


def transpose(matrix: list) -> list:
    dims = lengths(matrix)
    result = []

    # vector
    if dims[1] == 1:
        result.append(matrix)
    elif dims[0] == 1:
        return deepcopy(matrix[0])
    # matrix
    else:
        result = initialize(dims[0], dims[1])
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                result[row][col] = matrix[col][row]
    return result


def adjoint(matrix: list) -> list:
    dims = lengths(matrix)

    if dims[0] != dims[1]:
        raise Exception("Matrix must have the same number of columns and rows")

    result = initialize(dims[1], dims[0])

    for row in range(len(matrix)):
        for col in range(len(matrix[row])):
            cof = cofactor_adj(matrix, row, col)
            result[row][col] = cof

    result = transpose(result)

    return result