import unittest
import src.matrix_utils as mu


class TestMatrixUtils(unittest.TestCase):
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

    def test_sum_throw(self):
        m1 = [[1, 2, 3], [-1, 0]]
        m2 = [[2, -5, 0], [-2, 0, 1]]
        self.assertRaises(Exception, lambda: mu.sum(m1, m2))

    def test_mult(self):
        m1 = [[2, 3], [4, 6]]
        m2 = [[1, 3, 0], [2, 1, 1]]
        result = [[8, 9, 3], [16, 18, 6]]
        self.assertEqual(mu.mult(m1, m2), result)

    def test_mult_throw(self):
        m1 = [[-1, 3, 4], [2, 0, 1]]
        m2 = [[1, 2], [3, 4]]
        self.assertRaises(Exception, lambda: mu.mult(m1, m2))

    def test_determinant_2x2(self):
        m = [[1, 3], [2, 5]]
        result = -1
        self.assertEqual(mu.det(m), result)

    def test_determinant_3x3(self):
        m = [[1, 3, 0], [2, 5, 1], [2, 1, 3]]
        result = 2
        self.assertEqual(mu.det(m), result)
