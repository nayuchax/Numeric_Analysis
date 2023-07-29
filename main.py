from src import Least_squares_approximation
from src import Piecewise_quadrature
from src import Trapezoidal_rule
from src import Simpson_rule

import numpy as np
from numpy.linalg import solve

def relative_error(solution: float) -> float:
    exact_solution = 1.20919957615614523372938550509477048818
    e = (solution - exact_solution) / exact_solution
    return e

def absolute_error(solution: float) -> float:
    exact_solution = 1.20919957615614523372938550509477048818
    e = solution - exact_solution
    return e


def main():
    LIMIT = 0
    MAX = 1
    DIVIDE = 1000

    # 区分求積
    score = Piecewise_quadrature.piecewise_quadrature(LIMIT, MAX, DIVIDE)
    r_error = relative_error(score)
    a_error = absolute_error(score)
    print("区分求積法")
    print("計算結果=" + str(score))
    print("絶対誤差=" + str(a_error))
    print("相対誤差="+ str(r_error))

    # 台形公式
    score = Trapezoidal_rule.trapezoidal_rule(LIMIT, MAX, DIVIDE)
    r_error = relative_error(score)
    a_error = absolute_error(score)
    print("台形公式")
    print("計算結果=" + str(score))
    print("絶対誤差=" + str(a_error))
    print("相対誤差=" + str(r_error))

    #シンプソンの公式
    score = Simpson_rule.simpson_rule(LIMIT, MAX, DIVIDE)
    r_error = relative_error(score)
    a_error = absolute_error(score)
    print("シンプソン公式")
    print("計算結果=" + str(score))
    print("絶対誤差=" + str(a_error))
    print("相対誤差=" + str(r_error))

if __name__ == "__main__":
    main()
