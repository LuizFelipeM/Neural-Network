import unittest
import src.matrix_utils as mu


class TestMatrixUtils(unittest.TestCase):
    def test_initialize_matrix(self):
        result = [[1, 1], [1, 1], [1, 1]]
        self.assertEqual(mu.initialize(3, 2, 1), result)

    def test_initialize_vector(self):
        result = [0, 0, 0, 0, 0]
        self.assertEqual(mu.initialize(5, 1, 0), result)

    def test_initialize_line_vector(self):
        result = [[0, 0, 0, 0, 0]]
        self.assertEqual(mu.initialize(1,5,0), result)

    def test_validate_square_matrix(self):
        m = [1,2]
        self.assertRaises(Exception, lambda: mu.validate_square_matrix(m))

    def test_lengths(self):
        m = [[1, 2, 3]]
        result = (1, 3)
        self.assertEqual(mu.lengths(m), result)

    def test_lengths_scalar(self):
        e = 69
        self.assertRaises(Exception, lambda: mu.lengths(e))

    def test_is_scalar(self):
        e = [69]
        self.assertEqual(mu.is_scalar(e), True)

    def test_is_scalar_nested(self):
        e = [[69]]
        self.assertEqual(mu.is_scalar(e), True)

    def test_is_not_scalar_float(self):
        e = 69
        self.assertRaises(Exception, lambda: mu.is_scalar(e))

    def test_is_not_scalar_matrix(self):
        m = [[1, 2], [3, 4]]
        self.assertEqual(mu.is_scalar(m), False)

    def test_is_line_vector(self):
        v = [[1, 2, 3]]
        self.assertEqual(mu.is_line_vector(v), True)

    def test_is_not_line_vector(self):
        v = [1, 2, 3]
        self.assertEqual(mu.is_line_vector(v), False)

    def test_is_vector(self):
        v = [1, 2, 3]
        self.assertEqual(mu.is_vector(v), True)

    def test_is_not_vector(self):
        v = [[1, 2, 3]]
        self.assertEqual(mu.is_vector(v), False)

    def test_is_square(self):
        m = [[1, 2], [3, 4]]
        self.assertEqual(mu.is_square(m), True)

    def test_not_is_square(self):
        m = [1, 2]
        self.assertEqual(mu.is_square(m), False)

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

    def test_sum_line_vector(self):
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

    def test_mult_vector_result_scalar(self):
        m1 = [[1, 2, 3]]
        m2 = [1, 2, 3]
        result = [14]
        self.assertEqual(mu.mult(m1, m2), result)

    def test_mult_vector_result_square_matrix(self):
        m1 = [1, 2, 3]
        m2 = [[1, 2, 3]]
        result = [[1, 2, 3], [2, 4, 6], [3, 6, 9]]
        self.assertEqual(mu.mult(m1, m2), result)

    def test_mult_throw(self):
        m1 = [[-1, 3, 4], [2, 0, 1]]
        m2 = [[1, 2], [3, 4]]
        self.assertRaises(Exception, lambda: mu.mult(m1, m2))

    def test_mult_scalar_vector(self):
        e = [2]
        v = [1, 2, 3]
        result = [2, 4, 6]
        self.assertEqual(mu.mult(e, v), result)

    def test_mult_scalar_line_vector(self):
        e = [2]
        v = [[1, 2, 3]]
        result = [[2, 4, 6]]
        self.assertEqual(mu.mult(e, v), result)

    def test_mult_scalar_matrix(self):
        e = [2]
        m2 = [[1, 2], [3, 4]]
        result = [[2, 4], [6, 8]]
        self.assertEqual(mu.mult(e, m2), result)

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

    def test_transpose_line_vector(self):
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
