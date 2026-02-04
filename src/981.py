from number import fact_range, mod_inv
from functools import cache

M = 888_888_883 
FACT = fact_range(M, 3 * 88**3)


# much faster than mod_inv_range for not too many inverses
@cache
def inv(n):
    return mod_inv(n, M)

def N(X, Y, Z):
    n = X + Y + Z
    
    if not (X % 2 == Y % 2 == Z % 2):
        return 0

    r = (FACT[n] * inv(2) *
        inv(FACT[X]) * inv(FACT[Y]) * inv(FACT[Z])) % M

    # correction factor
    if n % 2 == 0:
        r += ((-1)**(n//2) * FACT[n//2] * inv(2) * 
              inv(FACT[X//2]) * inv(FACT[Y//2]) * inv(FACT[Z//2]))
            

    return r % M

s = 0
for i in range(88):
    for j in range(88):
        for k in range(88):
            s = (s + N(i**3, j**3, k**3)) % M
print(s)
