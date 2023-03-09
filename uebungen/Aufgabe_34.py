"""
sei z ein float nach IEEE-Standert half precision s10e5
1.
    Bias = 16-1 = 15, emin = -16+2 = -14, emax = 16-1 = 15
2.
    16Bit, 2Byte, V=vorzeichen, E=kodierter Exponent, M=Matrisse ohne Hidden Bit, VEEEEEMMMMMMMMMM
3.
    macheps = 1/1024
4.
    a)
        signed zero = v|00000|0000000000, signed inf = v|11111|0000000000
    b)
        kleinste normal number = 2**-14, größte normal number = 2¹⁵ * (1 + 1023/1024) ~ 2 ** 16
    c)
        kleinste subnormal = s.W. , größte subnormal = s.W.
    d)
        kleinste NaN = s.W. , größte NaN = s.W.
    e)
        0|01111|0000000001 = 1 * (2 ** (15 - 15)) * (1 + 1/1014)
    f)
        fl(-4) = 1|10001|0000000000
    g)
        fl(2/3) = 0|01110|0101010101
"""