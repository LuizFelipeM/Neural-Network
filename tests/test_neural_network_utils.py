import unittest
import utils.neural_network_utils as nu
from activation_enum import ActivationEnum


class TestNeuralNetworkUtils(unittest.TestCase):
    def test_activation_relu(self):
        val = 0.5
        expected = 0.5
        result = nu.get_activation_func(ActivationEnum.relu)
        self.assertEqual(result(val), expected)

    def test_activation_sigmoid(self):
        val = 5
        expected = 0.9933071490757153
        result = nu.get_activation_func(ActivationEnum.sigmoid)
        self.assertEqual(result(val), expected)

    def test_activate_layer(self):
        val = [[0, 0.2, 0.5], [1, 2, 3], [1, 0, 0]]
        expected = [[0, 0.2, 0.5], [1, 2, 3], [1, 0, 0]]
        result = nu.activate_layer(ActivationEnum.relu, val)
        self.assertEqual(result, expected)
