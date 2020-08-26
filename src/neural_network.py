import src.utils.matrix_utils as mu
import src.utils.neural_network_utils as nu
from random import uniform
from math import sqrt


class NeuralNetwork:
    biases = []
    weights_inp_hid = []
    weights_hid_out = []

    def __init__(self, input_quantity: int, hidden_quantity: int, output_quantity: int):
        self.weights_inp_hid = mu.functionoal_initialize(
            hidden_quantity,
            input_quantity,
            lambda *_: uniform(0, 1) * sqrt(2 / input_quantity)
        )

        self.weights_hid_out = mu.functionoal_initialize(
            output_quantity,
            hidden_quantity,
            lambda *_: uniform(0, 1) * sqrt(2 / hidden_quantity)
        )

        self.biases = mu.initialize(input_quantity + hidden_quantity + output_quantity, 1)

    def __feedforward(self, inputs: list):
        res_hid = mu.mult(inputs, self.weights_inp_hid)
        res_hid = mu.sum(res_hid, self.biases)
        res_hid = nu.activate_layer(res_hid)

        res_out = mu.mult(res_hid, self.weights_hid_out)
        res_out = mu.sum(res_out, self.biases)
        res_out = nu.activate_layer(res_out)


    # def __backpropagation(self):

    # def train(self, iterations, *inputs):
