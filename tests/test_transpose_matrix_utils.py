import unittest
import src.utils.matrix_utils as mu


class TestTransposeMatrix(unittest.TestCase):
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
