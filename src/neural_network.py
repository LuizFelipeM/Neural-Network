import src.utils.matrix_utils as mu
from random import uniform
from math import sqrt


class NeuralNetwork:
    biases = []
    weights_inp_hid = []
    weights_hid_out = []

    def __init__(self, input_quantity: int, hidden_quantity: int, output_quantity: int):
        weights_inp_hid = mu.functionoal_initialize(
            hidden_quantity,
            input_quantity,
            lambda *_: uniform(0, 1) * sqrt(2 / input_quantity)
        )

        weights_hid_out = mu.functionoal_initialize(
            output_quantity,
            hidden_quantity,
            lambda *_: uniform(0, 1) * sqrt(2 / hidden_quantity)
        )

        biases = mu.initialize(input_quantity + hidden_quantity + output_quantity, 1)

    # def feedforward(self, *inputs):

    # def backpropagation(self):

    # def train(self, *inputs):
