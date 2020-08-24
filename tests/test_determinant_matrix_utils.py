import unittest
import src.utils.matrix_utils as mu


class TestMatrixDeterminant(unittest.TestCase):
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
