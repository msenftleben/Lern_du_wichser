def sign(x):
    return (x > 0) - (x < 0)


def absolute(x):
    return x * sign(x)


def isclose(a, b, r_tol=1e-5, a_tol=1e-8):
    return absolute(a - b) <= (a_tol + r_tol * absolute(b))


def test_sign():
    assert sign(0) == 0
    assert sign(-4) == -1
    assert sign(4) == 1


def test_absolute():
    assert absolute(4) == 4
    assert absolute(-4) == 4
    assert absolute(0) == 0


def test_isclose():
    assert isclose(0.333333, 1/3) == 1
    assert isclose(3, 3) == 1
    assert isclose(2, 3) == 0


if __name__ == "__main__":
    test_isclose()
    test_absolute()
    test_sign()
