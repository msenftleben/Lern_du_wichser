def intersect(list_a, list_b):
    assert type(list_a) == list and type(list_b) == list
    intersected_list = []
    for item in list_a:
        if item in list_b and item not in intersected_list:
            intersected_list.append(item)
    return intersected_list


def test_intersect():
    assert intersect([1, 2, 3], [2, 3, 4]) == [2, 3]
    assert intersect([2, 3, 3, 3], [3, 4, 5, 6]) == [3]
    assert intersect([2, 3, 4, 1], []) == []


if __name__ == "__main__":
    test_intersect()
