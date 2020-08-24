from src.activation_enum import ActivationEnum
from math import exp


def activation(act_func: ActivationEnum, val: float) -> float:
    switcher = {
        ActivationEnum.relu: lambda x: max(0, x),
        ActivationEnum.sigmoid: lambda x: 1 / (1 + exp(- x))
    }
    func = switcher.get(act_func, lambda: "Invalid activation function")
    return func(val)
