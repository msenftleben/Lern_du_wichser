def deztoany(d, basis):
    assert basis <= 16
    digit_list = "0123456789ABCDEF"
    a = ""
    while True:
        a += digit_list[:basis][d % basis]
        d = d // basis
        if d == 0:
            break
    return a[::-1]


print(deztoany(24, 2))
