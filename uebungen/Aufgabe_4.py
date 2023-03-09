def maximum(values):
    assert type(values) == list
    assert len(values) > 0
    max_value = values[0]
    for value in values:
        if max_value < value:
            max_value = value
    return max_value


def test_maximum():
    assert maximum([1, 2, 3, 4]) == 4
    assert maximum([-1, 4, 2, 3.14]) == 4
    assert maximum([4, 4, 4, 3]) == 4


if __name__ == "__main__":
    test_maximum()
