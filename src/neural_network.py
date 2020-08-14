import src.matrix_utils as mu
from random import uniform
from math import sqrt


class NeuralNetwork:
    biases = []
    weights = []

    def __init__(self, input_quantity: int, hidden_quantity: int, output_quantity: int):
        weights = mu.initialize(
            hidden_quantity,
            input_quantity,
            lambda *_: uniform(0, 1) * sqrt(2/input_quantity))
        biases = weights
        # biases = mu.initialize(hidden_quantity, 1, randrange(0, 1))
