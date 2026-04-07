import os
import sys
import unittest

import numpy as np

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../src")))

from advanced_model import debye_integrand, gauss_legendre_integrate, debye_cv


class TestWeek06Bonus(unittest.TestCase):
    def test_integrand_zero_limit_points_8(self):
        v = debye_integrand(np.array([0.0]))[0]
        self.assertAlmostEqual(v, 1.0, places=8)

    def test_gauss_integrate_polynomial_points_12(self):
        try:
            val = gauss_legendre_integrate(lambda x: x**4, 0.0, 1.0, 8)
        except NotImplementedError as exc:
            self.fail(f"TODO D1 未完成: {exc}")
        self.assertLess(abs(val - 0.2), 1e-12)

    def test_debye_monotonic_points_10(self):
        try:
            c1 = debye_cv(20.0)
            c2 = debye_cv(80.0)
        except NotImplementedError as exc:
            self.fail(f"TODO D2 未完成: {exc}")
        self.assertGreater(c2, c1)


if __name__ == "__main__":
    unittest.main()
