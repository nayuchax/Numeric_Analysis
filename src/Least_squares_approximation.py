import numpy as np
from numpy.linalg import solve


# 最小二乗近似関数
def least_squares_approximation(
    x_arr: np.array, y_arr: np.array, x: float | int
) -> float:
    left_expr = np.array(
        [[len(x_arr), np.sum(x_arr)], [np.sum(x_arr), np.sum(x_arr**2)]]
    )

    right_expr = np.array([np.sum(y_arr), np.dot(x_arr, y_arr)])

    [a, b] = solve(left_expr, right_expr)
    return a + b * x
