def add(a, b):
    return float(a) + float(b)


def test_add():
    assert add(3, 3) == 6 and type(add(3, 3)) is float
    assert add(2.0, 3.1) == 5.1


if __name__ == "__main__":
    test_add()
