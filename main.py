from src import Least_squares_approximation
from src import Piecewise_quadrature
from src import Trapezoidal_rule
from src import Simpson_rule

import numpy as np
from numpy.linalg import solve


def main():
    """# 最小二乗近似
    x = np.array([0.5, 1, 1.5, 2])
    y = np.array([1.65, 2.72, 4.48, 7.39])
    target_x = 1.2

    print(Least_squares_approximation.least_squares_approximation(x, y, target_x))"""

    """# 区分求積
    LIMIT = 0
    MAX = 1
    DIVIDE = 4

    print(Piecewise_quadrature.piecewise_quadrature(LIMIT, MAX, DIVIDE))"""

    """# 台形公式
    LIMIT = 0
    MAX = 1
    DIVIDE = 4

    print(Trapezoidal_rule.trapezoidal_rule(LIMIT, MAX, DIVIDE))"""

    #シンプソンの公式
    LIMIT = 0
    MAX = 1
    DIVIDE = 4
    print(Simpson_rule.simpson_rule(LIMIT, MAX, DIVIDE))


if __name__ == "__main__":
    main()
