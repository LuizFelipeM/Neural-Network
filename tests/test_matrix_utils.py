import unittest
import src.matrix_utils as mu


class TestMatrixUtils(unittest.TestCase):
    def test_initialize_matrix(self):
        result = [[1,1],[1,1],[1,1]]
        self.assertEqual(mu.initialize(3,2,1), result)

    def test_initialize_vector(self):
        result = [0,0,0,0,0]
        self.assertEqual(mu.initialize(5,1,0), result)

    def test_initialize_column_vector(self):
        result = [[0,0,0,0,0]]
        self.assertEqual(mu.initialize(1,5,0), result)

    def test_lengths(self):
        m = [[1,2,3]]
        result = (1,3)
        self.assertEqual(mu.lengths(m), result)

    def test_lengths_escalar(self):
        n = 69
        self.assertRaises(Exception, lambda: mu.lengths(n))

    def test_sum(self):
        m1 = [[1, 2, 3], [-1, 0, 4]]
        m2 = [[2, -5, 0], [-2, 0, 1]]
        result = [[3, -3, 3], [-3, 0, 5]]
        self.assertEqual(mu.sum(m1, m2), result)

    def test_sum_vector(self):
        m1 = [1, 2, 3]
        m2 = [2, -5, 0]
        result = [3, -3, 3]
        self.assertEqual(mu.sum(m1, m2), result)

    def test_sum_column_vector(self):
        m1 = [[1, 2, 3]]
        m2 = [[3, 2, 1]]
        result = [[4, 4, 4]]
        self.assertEqual(mu.sum(m1, m2), result)

    def test_sum_throw(self):
        m1 = [[1, 2, 3], [-1, 0]]
        m2 = [[2, -5, 0], [-2, 0, 1]]
        self.assertRaises(Exception, lambda: mu.sum(m1, m2))

    def test_mult_matrices(self):
        m1 = [[2, 3], [4, 6]]
        m2 = [[1, 3, 0], [2, 1, 1]]
        result = [[8, 9, 3], [16, 18, 6]]
        self.assertEqual(mu.mult(m1, m2), result)

    def test_mult_vector_result_escalar(self):
        m1 = [[1, 2, 3]]
        m2 = [1, 2, 3]
        result = 14
        self.assertEqual(mu.mult(m1, m2), result)

    def test_mult_vector_result_square_matrix(self):
        m1 = [1, 2, 3]
        m2 = [[1, 2, 3]]
        result = [[1,2,3],[2,4,6],[3,6,9]]
        self.assertEqual(mu.mult(m1, m2), result)

    def test_mult_throw(self):
        m1 = [[-1, 3, 4], [2, 0, 1]]
        m2 = [[1, 2], [3, 4]]
        self.assertRaises(Exception, lambda: mu.mult(m1, m2))

    def test_determinant_2x2(self):
        m = [[2, 1], [2, 3]]
        result = 4
        self.assertEqual(mu.determinant(m), result)

    def test_determinant_3x3(self):
        m = [[2, 1, 3], [-1, 2, 1], [-2, 2, 3]]
        result = 15
        self.assertEqual(mu.determinant(m), result)

    def test_determinant_4x4(self):
        m = [[2, 5, -3, -2], [-2, -3, 2, -5], [1, 3, -2, 0], [-1, 6, 4, 0]]
        result = -103
        self.assertEqual(mu.determinant(m), result)

    def test_transpose_vector(self):
        m = [-1, 3, 4]
        result = [[-1, 3, 4]]
        self.assertEqual(mu.transpose(m), result)

    def test_transpose_column_vector(self):
        m = [[-1, 3, 4]]
        result = [-1, 3, 4]
        self.assertEqual(mu.transpose(m), result)

    def test_transpose_matrix(self):
        m = [[-1, 3, 4], [2, 0, 1], [1, 0, 5]]
        result = [[-1, 2, 1], [3, 0, 0], [4, 1, 5]]
        self.assertEqual(mu.transpose(m), result)

    def test_adjoint_matrix_2x2(self):
        m = [[1, 6], [4, 12]]
        result = [[12, -6], [-4, 1]]
        self.assertEqual(mu.adjoint(m), result)

    def test_adjoint_matrix_3x3(self):
        m = [[3, 1, -1], [2, -2, 0], [1, 2, -1]]
        result = [[2, -1, -2], [2, -2, -2], [6, -5, -8]]
        self.assertEqual(mu.adjoint(m), result)
