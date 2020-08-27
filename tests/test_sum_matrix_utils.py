import unittest
import utils.matrix_utils as mu


class TestSumMatrix(unittest.TestCase):
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
