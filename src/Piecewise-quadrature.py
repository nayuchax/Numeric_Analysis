import numpy as np

LIMIT = 0
MAX = 1
DIVIDE = 1000

# 区分求積法
def piecewise_quadrature (LIMIT: int, MAX: int, DIVIDE: int) -> float:
    s = 0
    h = float(1/DIVIDE)

    divide_ndarr = np.append(np.linspace(LIMIT, MAX, DIVIDE, endpoint=False), MAX)
    divide_list = divide_ndarr.tolist()
    divide_list = np.delete(divide_list, 0)
    for x in divide_list:
        s += h * func(x)
    return s
def func(x: float) -> float:
    fx = 1.0/(1.0 + x**2)
    return fx

print(piecewise_quadrature(LIMIT, MAX, DIVIDE))