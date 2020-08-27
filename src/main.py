import src.neural_network as nn

if __name__ == "__main__":
    neural_net = nn.NeuralNetwork(2, 3, 2)
    c = neural_net.train(1, [[1, 2]])
