import math
import os
import sys
import unittest

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from physics_model import f_diff, df_diff_true, f_int, int_true
from solver import forward_diff, central_diff, trapezoid, simpson, richardson


class TestWeek06Core(unittest.TestCase):
    def test_前差可运行_points_8(self):
        try:
            v = forward_diff(f_diff, 1.0, 1e-4)
        except NotImplementedError as exc:
            self.fail(f"TODO B1 未完成: {exc}")
        self.assertTrue(math.isfinite(v))

    def test_中心差分优于前差_points_10(self):
        x = 1.0
        h = 1e-3
        truth = df_diff_true(x)
        ef = abs(forward_diff(f_diff, x, h) - truth)
        ec = abs(central_diff(f_diff, x, h) - truth)
        self.assertLess(ec, ef)

    def test_trapezoid_polynomial_points_10(self):
        a, b = 0.0, 2.0
        truth = int_true(a, b)
        val = trapezoid(f_int, a, b, 200)
        self.assertLess(abs(val - truth), 5e-4)

    def test_simpson_polynomial_points_12(self):
        a, b = 0.0, 2.0
        truth = int_true(a, b)
        val = simpson(f_int, a, b, 100)
        self.assertLess(abs(val - truth), 1e-8)

    def test_simpson_even_constraint_points_10(self):
        with self.assertRaises(ValueError):
            simpson(f_int, 0.0, 2.0, 99)

    def test_richardson_improves_points_10(self):
        x = 1.0
        h = 1e-2
        truth = df_diff_true(x)
        d_h = central_diff(f_diff, x, h)
        d_h2 = central_diff(f_diff, x, h / 2)
        d_r = richardson(d_h, d_h2)
        self.assertLess(abs(d_r - truth), abs(d_h2 - truth))

    def test_鲁棒性输出有限数_points_10(self):
        x = 1.0
        for h in [1e-1, 1e-3, 1e-6]:
            self.assertTrue(math.isfinite(central_diff(f_diff, x, h)))


if __name__ == "__main__":
    unittest.main()
