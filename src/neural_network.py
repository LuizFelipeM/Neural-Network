from random import uniform
from math import sqrt
from activation_enum import ActivationEnum
import utils.matrix_utils as mu
import utils.neural_network_utils as nu


class NeuralNetwork:
    biases_hid = []
    biases_out = []
    weights_inp_hid = []
    weights_hid_out = []

    def __init__(self, input_quantity: int, hidden_quantity: int, output_quantity: int):
        self.weights_inp_hid = mu.functionoal_initialize(
            input_quantity,
            hidden_quantity,
            lambda *_: uniform(0, 1) * sqrt(2 / input_quantity)
        )

        self.weights_hid_out = mu.functionoal_initialize(
            hidden_quantity,
            output_quantity,
            lambda *_: uniform(0, 1) * sqrt(2 / hidden_quantity)
        )

        self.biases_hid = mu.initialize(1, hidden_quantity)
        self.biases_out = mu.initialize(1, output_quantity)

    def __feedforward(self, inputs: list):
        res_hid = mu.mult(inputs, self.weights_inp_hid)
        res_hid = mu.sum(res_hid, self.biases_hid)
        res_hid = nu.activate_layer(ActivationEnum.relu, res_hid)

        res_out = mu.mult(res_hid, self.weights_hid_out)
        res_out = mu.sum(res_out, self.biases_out)
        res_out = nu.activate_layer(ActivationEnum.sigmoid, res_out)

        return res_out

    # def __backpropagation(self):

    def train(self, iterations: int, *inputs):
        res = self.__feedforward(inputs[0])
        # for inp in inputs:
        #     self.__feedforward(inp)

        return res
