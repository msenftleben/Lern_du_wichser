def invert(perm):
    assert type(perm) == list
    inverted_liste = [0] * len(perm)
    for index, value in enumerate(perm):
        inverted_liste[value] = index
    return inverted_liste


def test_invert():
    assert invert([0, 1, 2, 3]) == [0, 1, 2, 3]
    assert invert([0, 2, 1]) == [0, 2, 1]
    assert invert([1, 2, 0]) == [2, 0, 1]


if __name__ == "__main__":
    test_invert()
