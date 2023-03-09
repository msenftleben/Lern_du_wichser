def bintooct(a):
    a = str(a)[2::][::-1]
    n = len(a)
    m = n // 3 + 1
    c = ""
    for k in range(m):
        c_current = 0
        for l in range(3):
            if 3 * k + l == n:
                break
            c_current += int(a[3 * k + l]) * 2 ** l
        c += str(c_current)
    return "0o"+c[::-1] if c else str(0), 8


def bintohex(a):
    hexChars = "0123456789abcdef"
    a = str(a)[2::][::-1]
    n = len(a)
    m = n // 4 + 1
    c = ""
    for k in range(m):
        c_current = 0
        for l in range(4):
            if 4 * k + l == n:
                break
            c_current += int(a[4 * k + l]) * 2 ** l
        c += hexChars[c_current]
    return "0x"+c[::-1] if c else str(0), 16


print(bintooct("0b1001"))
print(bin(int(* bintooct("0b1001"))))

print(bintohex("0b1111"))
print(bin(int(*bintohex("0b1111"))))
