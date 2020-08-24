import unittest
from src.utils.neural_network_utils import activation
from src.activation_enum import ActivationEnum


class TestNeuralNetworkUtils(unittest.TestCase):
    def test_activation_relu(self):
        val = 0.5
        expected = 0.5
        result = activation(ActivationEnum.relu, val)
        self.assertEqual(result, expected)

    def test_activation_sigmoid(self):
        val = 5
        expected = 0.9933071490757153
        result = activation(ActivationEnum.sigmoid, val)
        self.assertEqual(result, expected)