from copy import deepcopy


def initialize(y_dim, x_dim):
    result = []
    for y in range(y_dim):
        row = []
        for x in range(x_dim):
            row.append(0)
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
            result = matrix.copy()
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

    result = initialize(dims1[0], dims2[1])

    for row in range(len(matrix1)):
        for row2 in range(len(matrix2)):
            for col2 in range(len(matrix2[row2])):
                val1 = matrix1[row][row2]
                val2 = matrix2[row2][col2]
                result[row][col2] += val1 * val2

    return result


def det(matrix: list, row=0, col=0) -> float:
    result: float = 0
    sel_row: list
    cofacs: list = []
    dims = lengths(matrix)

    if dims[0] != dims[1]:
        raise Exception("Matrix must have the same number of columns and rows")

    if dims[0] == 2 and dims[1] == 2:
        result = matrix[0][0] * matrix[1][1] - matrix[0][1] * matrix[1][0]
    else:
        for detCol in range(len(matrix[row])):
            mat = deepcopy(matrix)
            sel_row = mat.pop(row)

            for rmRow in range(len(mat)):
                mat[rmRow].remove(mat[rmRow][detCol])

            cofacs.append(cof(det(mat), detCol + 1, row + 1))

        for el in sel_row:
            result += el * cofacs[sel_row.index(el)]

    return result


def cof(mnr: float, i: float, j: float) -> float:
    return (- 1)**(i + j) * mnr
