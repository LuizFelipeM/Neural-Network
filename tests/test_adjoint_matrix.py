import unittest
import utils.matrix_utils as mu


class TestAdjointMatrix(unittest.TestCase):
    def test_adjoint_matrix_2x2(self):
        m = [[1, 6], [4, 12]]
        result = [[12, -6], [-4, 1]]
        self.assertEqual(mu.adjoint(m), result)

    def test_adjoint_matrix_3x3(self):
        m = [[3, 1, -1], [2, -2, 0], [1, 2, -1]]
        result = [[2, -1, -2], [2, -2, -2], [6, -5, -8]]
        self.assertEqual(mu.adjoint(m), result)
