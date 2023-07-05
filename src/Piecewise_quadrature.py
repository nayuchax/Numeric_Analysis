import numpy as np


# 区分求積法
def piecewise_quadrature(LIMIT: int, MAX: int, DIVIDE: int) -> float:
    s = 0
    h = float((MAX-LIMIT) / DIVIDE)

    divide_ndarr = np.append(np.linspace(LIMIT, MAX, DIVIDE, endpoint=False), MAX)
    divide_list = divide_ndarr.tolist()
    divide_list = np.delete(divide_list, 0)
    for x in divide_list:
        s += h * func(x)
    return s


def func(x: float) -> float:
    fx = 1.0 / (1.0 + x**2)
    return fx
