"""
Sei z float nach parameter s2e2
1.
    B = 2 ** (2-1) - 1 = 1
    emin = 1-1 = 0
    emax = 2-1 = 1
2.
    es sind 5 Bits, 1 bit fürs Vorzeichen, 2 Bit für den kodierten Exponenten und 2 Bit für die Matrisse, V|EE|MM
3.
    macheps = 0.5 * 2 ** - (2 - 1) = 1/4
4.
    a)
        v|00|00 = 0, v|11|00 = inf
    b)
        0|01|00 = 0.25 kleinste positive normale Zahl
        0|10|11 = 2 * 0.5 = 1 größte positive normale Zahl
    c)
        0|00|00 = +0 kleinste positive subnormal
        0|00|11 = 0.5 + 0.25 = 0.75 größte positive subnormal
"""