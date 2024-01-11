from number import sieve
from functools import cache
from collections import Counter


suf = [Counter() for _ in range(28)]
primes = sieve(10**8)
pb = [set() for _ in range(28)]

for p in primes:
    bl = p.bit_length()
    pb[bl].add(p)

    # add to counter p's suffixes
    for i in range(bl+1):
        mask = (1 << i) - 1
        suf[i][p & mask] += 1

@cache
def E(x : int, b : int) -> float:
    """Maximized expected points given player knows lsb of prime x."""
    total = suf[b][x] - (x in pb[b])
    if total == 0: return 0

    x0 = x
    x1 = x | (1 << b)

    p0 = int(x0 in pb[b+1])
    p0m = (suf[b+1][x0] - p0)
    p1 = int(x1 in pb[b+1])
    p1m = (suf[b+1][x1] - p1)

    e0 = (p0 + p0m * (1 + E(x0,b+1)) + p1m * E(x1,b+1)) / total
    e1 = (p1 + p1m * (1 + E(x1,b+1)) + p0m * E(x0,b+1)) / total

    #print(x, e0, e1)
    return max(e0, e1)


print(round(E(0, 0), 8))