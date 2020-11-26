def test_save():
    file = open("./out/teste.csv", mode="w", encoding="utf-8")

    matrix = [
        [2, 5, -3, -2],
        [-2, -3, 2, -5],
        [1, 3, -2, 0],
        [-1, 6, 4, 0]
    ]

    file.write(str(matrix))
    file.close()
