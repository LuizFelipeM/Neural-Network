def lengths(matrix: list) -> tuple:
    x_dim = len(matrix)
    y_dim = len(matrix[0]) if isinstance(matrix[0], list) else 1
    return (x_dim, y_dim)


def is_square(matrix: list) -> bool:
    dim = lengths(matrix)
    return True if dim[0] == dim[1] and dim[0] != 1 else False


def validate_square_matrix(matrix: list):
    if not is_square(matrix) and not is_scalar(matrix):
        raise Exception("Matrix must have the same number of columns and rows")


def is_vector(matrix: list) -> bool:
    dim = lengths(matrix)
    return True if dim[0] != 1 and dim[1] == 1 else False


def is_line_vector(matrix: list) -> bool:
    dim = lengths(matrix)
    return True if dim[0] == 1 and dim[1] != 1 else False


def is_scalar(matrix: list) -> bool:
    dim = lengths(matrix)
    return True if dim[0] == 1 and dim[1] == 1 else False


def is_2d(matrix: list) -> bool:
    return isinstance(matrix[0], list)
