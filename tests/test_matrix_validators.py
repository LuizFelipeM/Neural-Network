import unittest
import src.validators.matrix_validators as mv
import src.utils.matrix_utils as mu


class TestMatrixValidators(unittest.TestCase):
    def test_lengths(self):
        m = [[1, 2, 3]]
        result = (1, 3)
        self.assertEqual(mv.lengths(m), result)

    def test_initialize_matrix(self):
        result = [[1, 1], [1, 1], [1, 1]]
        self.assertEqual(mu.initialize(3, 2, 1), result)

    def test_initialize_vector(self):
        result = [0, 0, 0, 0, 0]
        self.assertEqual(mu.initialize(5, 1, 0), result)

    def test_initialize_line_vector(self):
        result = [[0, 0, 0, 0, 0]]
        self.assertEqual(mu.initialize(1, 5, 0), result)

    def test_validate_square_matrix(self):
        m = [1, 2]
        self.assertRaises(Exception, lambda: mv.validate_square_matrix(m))

    def test_lengths_scalar(self):
        e = 69
        self.assertRaises(Exception, lambda: mv.lengths(e))

    def test_is_scalar(self):
        e = [69]
        self.assertEqual(mv.is_scalar(e), True)

    def test_is_scalar_nested(self):
        e = [[69]]
        self.assertEqual(mv.is_scalar(e), True)

    def test_is_not_scalar_float(self):
        e = 69
        self.assertRaises(Exception, lambda: mv.is_scalar(e))

    def test_is_not_scalar_matrix(self):
        m = [[1, 2], [3, 4]]
        self.assertEqual(mv.is_scalar(m), False)

    def test_is_line_vector(self):
        v = [[1, 2, 3]]
        self.assertEqual(mv.is_line_vector(v), True)

    def test_is_not_line_vector(self):
        v = [1, 2, 3]
        self.assertEqual(mv.is_line_vector(v), False)

    def test_is_vector(self):
        v = [1, 2, 3]
        self.assertEqual(mv.is_vector(v), True)

    def test_is_not_vector(self):
        v = [[1, 2, 3]]
        self.assertEqual(mv.is_vector(v), False)

    def test_is_square(self):
        m = [[1, 2], [3, 4]]
        self.assertEqual(mv.is_square(m), True)

    def test_not_is_square(self):
        m = [1, 2]
        self.assertEqual(mv.is_square(m), False)
