def sectohours(sec):
    assert type(sec) is int and sec >= 0, "bad_input_error"
    return "{:02d}:{:02d}:{:02d}".format(sec // 3600, sec // 60 - sec // 3600 * 60, sec % 60)


def test_sectohours():
    assert sectohours(50) == "00:00:50"
    assert sectohours(130) == "00:02:10"
    assert sectohours(3700) == "01:01:40"


if __name__ == "__main__":
    test_sectohours()
