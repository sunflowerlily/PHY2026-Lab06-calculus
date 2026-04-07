def forward_diff(f, x: float, h: float) -> float:
    # TODO B1
    raise NotImplementedError("TODO B1")


def backward_diff(f, x: float, h: float) -> float:
    # TODO B2
    raise NotImplementedError("TODO B2")


def central_diff(f, x: float, h: float) -> float:
    # TODO B3
    raise NotImplementedError("TODO B3")


def trapezoid(f, a: float, b: float, n: int) -> float:
    # TODO B4
    raise NotImplementedError("TODO B4")


def simpson(f, a: float, b: float, n: int) -> float:
    # TODO B5
    # 要求 n 为偶数，不满足应抛出 ValueError
    raise NotImplementedError("TODO B5")


def richardson(d_h: float, d_h2: float) -> float:
    # TODO B6
    raise NotImplementedError("TODO B6")
