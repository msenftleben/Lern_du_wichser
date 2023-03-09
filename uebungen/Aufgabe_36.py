"""
1.
    ein Eintrag == 64Bit or 8Byte
2.
    n²8 = 8*10⁶ ... n = 1000, ab n = 1000 wird der speicherplatz überschritten
3.
    tridiagonale matrix hat 3n-2 einträge, das CRS_Format brauch 2Einträge + (n+1) viele Plätze
    daraus ergebn sich 7n-3 viele plätze, also (7n-3)*8Byte, wenn jeder eintrag in double gespeichert wird
"""