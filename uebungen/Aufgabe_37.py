def har(n):
    list_ascending = [i for i in range(n)][1:]
    list_decreasing = list_ascending[::-1]
    value_ascending = 0
    value_decreasing = 0
    for i in list_ascending:
        value_ascending += 1/i
    for i in list_decreasing:
        value_decreasing += 1/i
    return value_ascending, value_decreasing


print(har(100000))
