def dot(vec1, vec2):
    assert type(vec1) is dict and type(vec2) is dict
    dot_product = 0
    for indicator in vec1:
        if indicator in vec2:
            dot_product += vec1[indicator] * vec2[indicator]
    return dot_product


def scalevec(scalar, vec):
    assert type(scalar) == int or float
    assert type(vec) is dict
    if scalar == 0:
        return {}
    for indicator in vec:
        vec[indicator] *= scalar
    return vec


def sumvec(vec1, vec2):
    assert type(vec1) is dict and type(vec2) is dict
    summevec = vec1.copy()
    indicator = vec2.copy()
    for index in indicator:
        nextsum = indicator[index] + summevec.pop(index, 0)
        if nextsum != 0:
            summevec[index] = nextsum
    return summevec


def test_dot():
    assert dot({}, {}) == 0
    assert dot({1: 2, 2: 3, 3: 4}, {2: 3, 3: 4, 4: 5}) == 25
    assert dot({0: 1, 2: 2, 4: 4}, {1: 2, 3: 3, 5: 2}) == 0


def test_scalevec():
    assert scalevec(0, {1: 2, 2: 3}) == {}
    assert scalevec(2, {1: 2, 2: 3, 3: 4}) == {1: 4, 2: 6, 3: 8}
    assert scalevec(1, {}) == {}


def test_sumvec():
    assert sumvec({1: 2, 2: 3, 3: 4}, {1: 2, 2: 3, 3: 4}) == {1: 4, 2: 6, 3: 8}
    assert sumvec({1: 2, 2: 3}, {}) == {1: 2, 2: 3}
    assert sumvec({1: -1, 2: -2, 3: -3}, {1: 1, 2: 2, 3: 3}) == {}


if __name__ == "__main__":
    test_scalevec()
    test_sumvec()
    test_dot()
