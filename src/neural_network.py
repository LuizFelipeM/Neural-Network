from random import uniform
from math import sqrt
from src.activation_enum import ActivationEnum
import src.utils.matrix_utils as mu
import src.utils.neural_network_utils as nu


class NeuralNetwork:
    learning_ratio = 0.3
    biases_hid = []
    biases_out = []
    weights_inp_hid = []
    weights_hid_out = []

    def __init__(self, input_quantity: int, hidden_quantity: int, output_quantity: int):
        self.weights_inp_hid = mu.functional_initialize(
            input_quantity,
            hidden_quantity,
            lambda *_: uniform(0, 1) * sqrt(2 / input_quantity)
        )

        self.weights_hid_out = mu.functional_initialize(
            hidden_quantity,
            output_quantity,
            lambda *_: uniform(0, 1) * sqrt(2 / hidden_quantity)
        )

        self.biases_hid = mu.initialize(1, hidden_quantity)
        self.biases_out = mu.initialize(1, output_quantity)

    def __feedforward_hid(self, inputs: list):
        net = mu.mult(inputs, self.weights_inp_hid)
        net = mu.sum(net, self.biases_hid)
        res = nu.activate_layer(ActivationEnum.relu, net)

        return net, res

    def __feedforward_out(self, inputs: list):
        net = mu.mult(inputs, self.weights_hid_out)
        net = mu.sum(net, self.biases_out)
        res = nu.activate_layer(ActivationEnum.sigmoid, net)

        return net, res

    # def __backpropagation_core(self):

    # def __backpropagation(self, exp):

    def train(self, iterations: int, *inputs):
        # res = self.__feedforward(inputs[0])
        # for inp in inputs:
        #     self.__feedforward(inputs)
