def isdecreasing(list_to_test):
    assert type(list_to_test) == list
    for previndex, value in enumerate(list_to_test[1:]):
        if list_to_test[previndex] < value:
            return False
    return True


def sort_decreasing(list_to_order):
    assert type(list_to_order) is list
    sorted_list = list_to_order.copy()
    for index in range(len(sorted_list), 1, -1):
        for pairindex in range(index - 1):
            pair = sorted_list[pairindex:pairindex + 2]
            if not isdecreasing(pair):
                sorted_list[pairindex:pairindex + 2] = pair[::-1]
    return sorted_list


def test_sort_decreasing():
    assert sort_decreasing([2, 1, 3, 4]) == [4, 3, 2, 1]
    assert sort_decreasing([2, 3, 3, 3]) == [3, 3, 3, 2]
    assert sort_decreasing([-1, 3.1415, 3]) == [3.1415, 3, -1]


if __name__ == "__main__":
    test_sort_decreasing()
