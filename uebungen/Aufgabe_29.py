"""
1.
    a)
        (10101010)2 + (11100000)2 = (110001010)2
    b)
        (23)7 + (16)7 = (42)7
    c)
        (19)h + (12)h = (2B)h
2.
    a)
        i)
            (10101010)Z = -128 + 32 + 8 + 2 = -86
        ii)
            (11100000)Z = -128 + 64 + 32 = -32
    b)
        carry flag = carry(N-1, N) = 1, overflow flag = carry(N-2, N-1) = 1,
        da carry flag = 1 ==> unsigned X, da carry flag + overflow flag = 1 + 1 = 0 ==> signed OK
3.
    N = 4
        x = 7 = (0111)Z
        x = -7 = (1001)Z
    N = 6
        x = 7 = (000111)Z
        x = -7 = (111001)Z
"""