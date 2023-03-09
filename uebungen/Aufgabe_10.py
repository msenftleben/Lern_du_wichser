def isdecreasing(list_to_test):
    assert type(list_to_test) == list
    for previndex, value in enumerate(list_to_test[1:]):
        if list_to_test[previndex] < value:
            return False
    return True


def insertinplace(newscore, scores):
    assert type(newscore) is int
    assert type(scores) is list
    assert isdecreasing(scores) == 1
    counter = 0
    if len(scores) == 0:
        scores.insert(counter, newscore)
        return scores
    else:
        while counter < len(scores):
            if newscore >= scores[counter]:
                break
            counter += 1
        if scores[counter] != newscore:
            scores.insert(counter, newscore)
        return scores


def test_insertinplace():
    assert insertinplace(3, [4, 3, 2, 1]) == [4, 3, 2, 1]
    assert insertinplace(2, [4, 3, 1]) == [4, 3, 2, 1]
    assert insertinplace(3, []) == [3]


if __name__ == "__main__":
    test_insertinplace()
