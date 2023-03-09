"""nur 2. und 3. (1. vergleichbar)"""


def heron(a, x, maxiter, tol=1e-10):
    assert type(a) == int or float
    assert a > 0 and x > 0
    assert type(maxiter) is int
    assert type(x) == int or float
    list_k_tol = []
    for k in range(maxiter):
        k_tol = abs(x - a ** 0.5)
        list_k_tol.append(k_tol)
        if k_tol < tol:
            break
        x = (x ** 2 + a) / (2 * x)
    return x, len(list_k_tol), list_k_tol


def isclose(a, b):
    return abs(a - b) < 1e-8


def test_heron():
    assert isclose(heron(4, 1, 1000)[0], 2) == 1
    assert isclose(heron(9, 1, 1000)[0], 3) == 1
    assert isclose(heron(3, 1, 1000)[0], 5) == 0


if __name__ == "__main__":
    test_heron()
