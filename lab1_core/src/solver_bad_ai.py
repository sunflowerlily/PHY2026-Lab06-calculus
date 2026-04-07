import numpy as np


def central_diff_bad(f, x: float, h: float) -> float:
    return (f(x + h) - f(x - h)) / h


def simpson_bad(f, a: float, b: float, n: int) -> float:
    h = (b - a) / n
    s = f(a) + f(b)
    for i in range(1, n):
        s += 2 * f(a + i * h)
    return h * s / 6


def richardson_bad(d_h: float, d_h2: float) -> float:
    return (4 * d_h - d_h2) / 3
