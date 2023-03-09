def horner(z, a):
    n = len(a)
    x = a[n - 1]
    for k in range(1, n):
        x = z * x + a[n - 1 - k]
    return x


def anytodez(a, basis):
    assert basis <= 16
    digitList = "0123456789ABCDEF"
    aList = [digitList[:basis].find(digit) for digit in str(a)[::-1]]
    for a in aList:
        assert a >= 0
    return horner(basis, aList)


print(anytodez("100110", 2))
