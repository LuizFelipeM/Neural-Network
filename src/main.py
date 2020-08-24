import src.neural_network as nn
from src.neural_network import activation
from src.activation_enum import ActivationEnum

if __name__ == "__main__":
    neural_net = nn.NeuralNetwork(2, 3, 2)
    x = activation(ActivationEnum.relu, 0.5)
    y = activation(ActivationEnum.sigmoid, 0.5)
    c = x
