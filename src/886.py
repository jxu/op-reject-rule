from functools import cache
from math import gcd

def coprime(a, b):
    return gcd(a, b) == 1

def count_even(s):
    return (s & 0x555555555).bit_count()

def count_odd(s):
    return (s & 0xaaaaaaaaa).bit_count()

N = 34

cp = [[False]*(N+1) for _ in range(N+1)]

for i in range(2, N+1):
    for j in range(2, N+1):
        cp[i][j] = coprime(i, j)


def P(n):
    @cache
    def f(seen, i):

        if seen == (1 << i): 
            return 1

        # try some even-odd parity
        evens = count_even(seen)
        odds = count_odd(seen)
        l = seen.bit_count()

        if l % 2 == 1:
            if not (i % 2 == 0 and evens - odds == 1): return 0
        else:
            if not (i % 2 == 1 and evens - odds == 0): return 0

        r = 0
        for j in range(2, n+1):
            if (seen & (1 << j)) and cp[i][j]:
                r += f(seen & ~(1 << i), j)

        return r

    r = 0
    full = ((1 << (n+1)) - 1) & ~3
    print(bin(full))

    for k in range(2, n+1):
        z = f(full, k)
        print(k, z)
        r += z

    # P(20)
    # no cond: hits=12271501, misses=2831840
    #    cond: hits= 3483249, misses=1214491

    print(f.cache_info())
    return r 

print(P(20))
