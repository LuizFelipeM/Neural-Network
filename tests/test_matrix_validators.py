import unittest
import src.matrix_validators as mv


class TestMatrixValidators(unittest.TestCase):
    def test_lengths(self):
        m = [[1, 2, 3]]

        result = (1, 3)

        self.assertEqual(mv.lengths(m), result)
