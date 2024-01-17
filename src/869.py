from number import sieve
from functools import cache
from collections import Counter

N = 10**8
B = N.bit_length()
suf = [Counter() for _ in range(B+1)]
primes = sieve(N)
pb = [set() for _ in range(B+1)]

print("primes")

for p in primes:
    bl = p.bit_length()
    pb[bl].add(p)

    # add to counter p's suffixes
    for i in range(bl+1):
        mask = (1 << i) - 1
        suf[i][p & mask] += 1

print("test")

def E(x : int, b : int) -> float:
    """Maximized expected points given player knows lsb of prime x."""
    if b == B: return 0
    total = suf[b][x]
    if total == 0: return 0

    x0 = x
    x1 = x | (1 << b)

    p0m = suf[b+1][x0]
    p1m = suf[b+1][x1]

    e0, e1 = E(x0, b+1), E(x1, b+1)
    g0 = p0m * (1 + e0) + p1m * e1
    g1 = p1m * (1 + e1) + p0m * e0

    return max(g0, g1) / total


print(round(E(0, 0), 8))