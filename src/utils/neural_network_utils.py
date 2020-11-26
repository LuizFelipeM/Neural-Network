from src.activation_enum import ActivationEnum
from math import exp


def sigmoid(x):
    return 1 / (1 + exp(- x))


def get_activation_func(act_func: ActivationEnum):
    switcher = {
        ActivationEnum.relu: lambda x: max(0, x),
        ActivationEnum.sigmoid: lambda x: sigmoid(x)
    }
    func = switcher.get(act_func, lambda: "Invalid activation function")
    return func


def get_activation_derivative_func(act_func: ActivationEnum):
    switcher = {
        ActivationEnum.relu: lambda x: 0 if x <= 0 else 1,
        ActivationEnum.sigmoid: lambda x: sigmoid(x) * (1 - sigmoid(x))
    }
    func = switcher.get(act_func, lambda: "Invalid activation function")
    return func


def activate_layer(act_func: ActivationEnum, layer: list) -> list:
    func = get_activation_func(act_func)
    res = list(map(lambda row: list(map(func, row)), layer))
    return res
