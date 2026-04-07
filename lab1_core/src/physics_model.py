import math


def f_diff(x: float) -> float:
    return math.sin(x)


def df_diff_true(x: float) -> float:
    return math.cos(x)


def d2f_diff_true(x: float) -> float:
    return -math.sin(x)


def f_int(x: float) -> float:
    return x**4 - 2.0 * x + 1.0


def f_int_antiderivative(x: float) -> float:
    return x**5 / 5.0 - x**2 + x


def int_true(a: float, b: float) -> float:
    return f_int_antiderivative(b) - f_int_antiderivative(a)


def abs_error(estimate: float, truth: float) -> float:
    return abs(estimate - truth)
