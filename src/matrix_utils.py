def matrix_sum(*matrices):
    value = 0

    for row in matrices[0]:
        for cell in row:
            value += cell

    return value
