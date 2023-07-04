import numpy as np


# 台形公式
def trapezoidal_rule(LIMIT: int, MAX: int, DIVIDE: int) -> float:
    s = 0
    h = float(1 / DIVIDE) / 2

    divide_ndarr = np.append(np.linspace(LIMIT, MAX, DIVIDE, endpoint=False), MAX)
    divide_list = divide_ndarr.tolist()
    for i in range(0, DIVIDE):
        s += h * (func(divide_list[i]) + func(divide_list[i + 1]))
    return s


def func(x: float) -> float:
    fx = x**3
    return fx
