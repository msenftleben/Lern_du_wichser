def add(a, b, basis):
    assert basis <= 16
    digitlist = "0123456789abcdef"
    a = [digitlist[:basis].find(el) for el in a][::-1]
    b = [digitlist[:basis].find(el) for el in b][::-1]
    for el in a:
        assert el >= 0
    for el in b:
        assert el >= 0
    if len(a) < len(b):
        b, a = a, b
    c = ""
    carry = 0
    for k, el in enumerate(b):
        s = a[k] + b[k] + carry
        s_mod = s % basis
        carry = s // basis
        c += digitlist[:basis][s_mod]
    for l in range(len(b) + 1, len(a)):
        s = a[l] + carry
        s_mod = s % basis
        carry = s // basis
        c += digitlist[:basis][s_mod]
    if carry:
        c += digitlist[:basis][carry]
    return c[::-1]


print(add("e", "f", 16))
