def square(x):
    return x ** 2


def test_square():
    assert square(2.) == 4
    assert square(-1) == 1


if __name__ == "__main__":
    test_square()
