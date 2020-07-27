def lengths(matrix):
    xDim = len(matrix)
    yDim = len(matrix[0]) if isinstance(matrix[0], list) else 1
    return (xDim, yDim)


def sum(*matrices):
    dims = lengths(matrices[0])
    for matrix in matrices:
        if dims[0] != lengths(matrix)[0] or dims[1] != lengths(matrix)[1]:
            raise Exception("Matrices' lengths do not match! \n\n" + str(lengths(matrix)) + str(lengths(matrices[0])))

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
