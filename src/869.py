from number import sieve
from functools import cache

primes = set(bin(n)[2:] for n in sieve(10))
print(primes)
np = len(primes)

@cache
def E(x, more=True):
    #if len(x) > 3: return 0
    total = sum(p.endswith(x) and p != x for p in primes)
    #print("x", x, "total", total)
    if total == 0: return 0

    x0 = "0" + x
    x1 = "1" + x
    p0 = int(x0 in primes) / total
    p0m = (sum(p.endswith(x0) and p != x0 for p in primes)) / total
    p1 = int(x1 in primes) / total
    p1m = (sum(p.endswith(x1) and p != x1 for p in primes)) / total


    #print(p0, p0m, p1, p1m)

    e0 = p0 + p0m * (1 + E(x0)) + p1m * E(x1)
    e1 = p1 + p1m * (1 + E(x1)) + p0m * E(x0)

    print(x, p0, p0m, p1, p1m, e0, e1, max(e0, e1), sep='\t\t')
    return max(e0, e1)

print(E(""))