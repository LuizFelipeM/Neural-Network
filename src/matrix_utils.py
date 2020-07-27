def lengths(matrix):
    xDim = len(matrix)
    yDim = len(matrix[0]) if isinstance(matrix[0], list) else 1
    return (xDim, yDim)


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
        if result == []:
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

def mult(matrice1, matrice2):
    dims1 = lengths(matrice1)
    dims2 = lengths(matrice2)

    if dims1[1] != dims2[0]:
        raise Exception("Matrices' row and column does not match! \n\n"
                        + str(lengths(matrice1))
                        + str(lengths(matrice2))
                        )

    result = [[0]*dims2[1]]*dims1[0]

    for row in range(len(matrice1)):
        for row2 in range(len(matrice2)):
            for cell in range(len(matrice2[row2])):
                result[row][cell] += matrice1[row][cell] * matrice2[cell][row2]

    return result

    # [1, 2]    [-1, 3]
    # [3, 4] x  [ 4, 2]


x = mult([[2, 3], [0, 1], [-1, 4]], [[1, 2, 3], [-2, 0, 4]])
