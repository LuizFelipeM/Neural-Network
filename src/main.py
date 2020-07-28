import matrix_utils as mu

if __name__ == "__main__":
    # res = mu.mult(trans, [1,2,3])

    m = [[-1, 3, 4], [2, 0, 1], [1, 0, 5]]
    trans = mu.transpose(m)
    result = [[-1, 2, 1], [3, 0, 0], [4, 1, 5]]

    print(result)
    print("hola")
