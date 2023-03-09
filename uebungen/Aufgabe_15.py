def ggt_iterativ(a, b):
    assert type(a) is int and a > 0
    assert type(b) is int and b > 0
    while b != 0:
        h = a % b
        a = b
        b = h
    return a


def ggt_rekusiv(a, b):
    assert type(a) is int and a > 0
    assert type(b) is int and b >= 0
    if b == 0:
        return a
    else:
        return ggt_rekusiv(b, a % b)


def test_ggt_iterativ():
    assert ggt_iterativ(32, 16) == 16
    assert ggt_iterativ(12, 123) == 3
    assert ggt_iterativ(5, 7) == 1


def test_ggt_rekusiv():
    assert ggt_rekusiv(32, 16) == 16
    assert ggt_rekusiv(12, 123) == 3
    assert ggt_rekusiv(5, 7) == 1


if __name__ == "__main__":
    test_ggt_rekusiv()
    test_ggt_iterativ()
