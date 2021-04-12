from typing import NamedTuple

import numpy as np
from numpy import ndarray, random

WBGrad = NamedTuple("WBGrad", [("w", ndarray), ("b", ndarray)])


class Linear(object):
    def __init__(self, m: int, n: int):
        """
        Y = F(X) + B,
        Y, B: R^n
        F:    R^m -> R^n
        X:    R^m
        Random initialization
        """
        self.W = random.randn(m, n)
        self.B = random.randn(n)

    def __call__(self, X: ndarray):
        "Using this object as a function"
        return self.W @ X + self.B

    # Continued from the previous definition

    @staticmethod
    def loss_func(x: ndarray, y: ndarray) -> float:
        "Calculate the loss between `x` and `y`"
        squared = (x - y) ** 2
        return squared.sum().item()

    def loss(self, real_x: ndarray, real_y: ndarray) -> float:
        "Calculate the loss given a pair of real data"

        # Calling the above defined `__call__` method
        pred_y = self(real_x)

        # See how far the predict value is from the real value
        # That is how good your model is
        return self.loss_func(pred_y, real_y)

    # Continued from the previous definition

    def gradient(self, real_x: ndarray, real_y: ndarray) -> Tuple[ndarray]:
        "Calculate the gradient"

        # Calling the above defined `__call__` method
        pred_y = self(real_x)

        # Getting the element-wise difference
        diff = pred_y - real_y

        # partial L / partial W_ij = diff_i * x_j
        W_grad = real_x.T @ diff

        # partial L / partial B_i = diff_i
        B_grad = diff

        return WBGrad(w=W_grad, b=B_grad)

    def train(self, real_x: ndarray, real_y: ndarray, lr: float):
        "This is what people call training a model"
        grad = self.gradient(real_x, real_y)

        # updating the parameters
        self.W -= lr * grad.w
        self.B -= lr * grad.b
