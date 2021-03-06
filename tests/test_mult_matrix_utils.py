import unittest
import src.matrix_utils as mu


class TestMultMatrix(unittest.TestCase):
    def test_mult_throw(self):
        m1 = [[-1, 3, 4], [2, 0, 1]]
        m2 = [[1, 2], [3, 4]]

        self.assertRaises(Exception, lambda: mu.mult(m1, m2))

    def test_mult_2x2_2x3(self):
        m1 = [[2, 3], [4, 6]]
        m2 = [[1, 3, 0], [2, 1, 1]]
        result = [[8, 9, 3], [16, 18, 6]]
        self.assertEqual(mu.mult(m1, m2), result)
