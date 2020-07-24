import unittest
from src.matrix_utils import matrix_sum


class TestMatrixUtils(unittest.TestCase):
    def test_sum(self):
        m1 = [[1, 2, 3], [-1, 0, 4]]
        m2 = [[2, 5, 0], [-2, 0, 1]]
        result = [[3, -3, 3], [-3, 0, 5]]

        self.assertEqual(matrix_sum(m1, m2), result)
