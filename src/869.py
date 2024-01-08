from number import sieve
from functools import cache
from collections import Counter

suf = Counter()
primes = sieve(10**8)
pb = set()
for p in primes:
    s = bin(p)[2:]
    pb.add(s)
    for i in range(len(s)+1):
        suf[s[i:]] += 1

#print(suf)

@cache
def E(x):
    total = suf[x] - (x in pb)
    #print("x", x, "total", total)
    if total == 0: return 0

    x0 = "0" + x
    x1 = "1" + x
    p0 = (x0 in pb) / total
    p0m = (suf[x0] - (x0 in pb)) / total
    p1 = (x1 in pb) / total
    p1m = (suf[x1] - (x1 in pb)) / total


    e0 = p0 + p0m * (1 + E(x0)) + p1m * E(x1)
    e1 = p1 + p1m * (1 + E(x1)) + p0m * E(x0)

    #print(x, p0, p0m, p1, p1m, e0, e1, max(e0, e1), sep='\t\t')
    print(x, e0, e1)
    return max(e0, e1)

print(round(E(""),8))