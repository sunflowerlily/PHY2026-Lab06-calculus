import numpy as np


def debye_integrand(x):
    x = np.asarray(x)
    out = np.empty_like(x, dtype=float)
    small = np.abs(x) < 1e-10
    out[small] = 1.0
    xs = x[~small]
    ex = np.exp(xs)
    out[~small] = xs**4 * ex / (ex - 1.0) ** 2
    return out if out.shape else float(out)


def gauss_legendre_integrate(func, a: float, b: float, n: int) -> float:
    # TODO D1
    raise NotImplementedError("TODO D1")


def debye_cv(T: float, theta_d: float = 428.0, n_nodes: int = 64) -> float:
    # TODO D2
    raise NotImplementedError("TODO D2")


def cv_scan(T_values, theta_d: float = 428.0, n_nodes: int = 64):
    return np.array([debye_cv(T, theta_d=theta_d, n_nodes=n_nodes) for T in T_values])
