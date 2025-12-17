from number import is_square
from math import isqrt

M = 50

for a in range(2, M+1):
    for b in range(a+1, M+1):
        if is_square(a**2 + b**2 - 1):
            c = isqrt(a**2 + b**2 - 1)
            print(a, b, c)
