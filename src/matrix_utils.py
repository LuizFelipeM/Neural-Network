def matrix_sum(*matrices):
    value = matrices[0].copy()
    biggestLen = 0

    for matrix in matrices:
        for row in matrix:
            if len(row) > biggestLen:
                biggestLen = len(row)

    for matrix in matrices:
        for row in matrix:
            if len(row) != biggestLen:
                raise Exception("Error - matrices has different lengths")

    for matrix in matrices:
        if matrices.index(matrix) == 0:
            continue

        for row in value:
            rowMatrix = matrix[value.index(row)]
            for cell in rowMatrix:
                value[value.index(row)][rowMatrix.index(cell)] += cell

    return value
