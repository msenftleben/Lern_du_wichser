def intersect(list_a, list_b):
    assert type(list_a) is list and type(list_b) is list
    intersected_list = []
    for item in list_a:
        if item in list_b and item not in intersected_list:
            intersected_list.append(item)
    return intersected_list


def test_intersected_list():
    assert intersect([1, 2, 4, 5], [2, 4, 5, 6]) == [2, 4, 5]
    assert intersect([1], [1, 2, 3]) == [1]


if __name__ == "__main__":
    test_intersected_list()
