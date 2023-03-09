def isdecreasing(list_to_test):
    assert type(list_to_test) is list
    for previndex, value in enumerate(list_to_test):
        if not list_to_test[previndex] >= value:
            return False
    return True


def insertinplace(newscore, scores):
    assert type(newscore) == int or float
    assert isdecreasing(scores) == 1
    assert type(scores) is list
    counter = 0
    if len(scores) == 0:
        scores.insert(counter, newscore)
        return scores
    else:
        while counter < len(scores):
            if scores[counter] <= newscore:
                break
            counter += 1
        if scores[counter] != newscore:
            scores.insert(counter, newscore)
        return scores


def test_insertinplace():
    assert insertinplace(3, [5, 4, 2, 1]) == [5, 4, 3, 2, 1]
    assert insertinplace(8, []) == [8]
    assert insertinplace(3, [6, 5, 4, 3, 2, 1]) == [6, 5, 4, 3, 2, 1]


if __name__ == "__main__":
    test_insertinplace()