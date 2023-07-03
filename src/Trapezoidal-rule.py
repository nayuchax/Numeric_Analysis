import numpy as np

LIMIT = 0
MAX = 1
DIVIDE = 4

# 区分求積法
def piecewise_quadrature (LIMIT: int, MAX: int, DIVIDE: int):
    s = 0
    h = float(1/DIVIDE) / 2

    divide_ndarr = np.append(np.linspace(LIMIT, MAX, DIVIDE, endpoint=False), MAX)
    divide_list = divide_ndarr.tolist()
    for i in range(0,DIVIDE):
        s += h * (func(divide_list[i]) +func(divide_list[i+1]))
    return s
def func(x: float) -> float:
    fx = x**3
    return fx

print(piecewise_quadrature(LIMIT, MAX, DIVIDE))
