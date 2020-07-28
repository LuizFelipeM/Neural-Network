def initialize(dimY, dimX, defaultValue = 0):
    if dimY == 1 and dimX == 1:
        return defaultValue

    result = []
    for y in range(dimY):
        row = []
        for x in range(dimX):
            row.append(defaultValue)
        result.append(row)
    return result

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

def mult(matrix1, matrix2):
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

    # [1, 2]    [-1, 3]
    # [3, 4] x  [ 4, 2]


x = mult([[2, 3], [0, 1], [-1, 4]], [[1, 2, 3], [-2, 0, 4]])

def transpose(matrix):
    dims = lengths(matrix)
    if dims[0] != dims[1]:
        raise Exception("Cant transpose a matrix which is not squared -->")
        print(matrix)

    isVector = not isinstance(matrix[0], list)

    result = []
    if isVector:
        result.append(matrix)
    else:
        result = matrix[:][:]
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                if (row != col):
                    result[row][col] = matrix[col][row]
                    # result[row][col] = 3
    return result

