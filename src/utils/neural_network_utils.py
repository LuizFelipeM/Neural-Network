from src.activation_enum import ActivationEnum
from math import exp


def get_activation_func(act_func: ActivationEnum):
    switcher = {
        ActivationEnum.relu: lambda x: max(0, x),
        ActivationEnum.sigmoid: lambda x: 1 / (1 + exp(- x))
    }
    func = switcher.get(act_func, lambda: "Invalid activation function")
    return func


def activate_layer(act_func: ActivationEnum, layer: list) -> list:
    func = get_activation_func(act_func)
    res = list(map(lambda row: list(map(func, row)), layer))
    return res
