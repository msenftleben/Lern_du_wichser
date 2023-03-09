def horner(z, a):
    n = len(a)
    x = a[n-1]
    for k in range(1, n):
        x = z * x + a[n-1-k]
    return x


print(horner(2, [1, 2, 2]))
