def fib(n):
    x0 = 0
    x1 = 1
    if n == 0 or n == 1:
        return n
    for i in range(n-1):
        x2 = x1 + x0
        x0 = x1
        x1 = x2
    return x1


def test_fib():
    assert fib(0) == 0
    assert fib(2) == 1
    assert fib(4) == 3


if __name__ == "__main__":
    test_fib()
