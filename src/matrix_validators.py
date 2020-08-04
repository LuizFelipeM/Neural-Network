def lengths(matrix):
    x_dim = len(matrix)
    y_dim = len(matrix[0]) if isinstance(matrix[0], list) else 1
    return (x_dim, y_dim)