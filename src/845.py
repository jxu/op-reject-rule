from number import sieve
from functools import cache

primes = sieve(10000)

@cache
def c(s, d):
    #print(s, d)
    if s < 0: return 0
    assert d >= 0
    if d == 0: return int(s == 0)
    return sum(c(s-i, d-1) for i in range(10))

def q(n, s):
    digits = [int(c) for c in str(n)]
    nd = len(digits)-1
    old_s = s
    r = 0
    for i in range(len(digits)):
        d = digits[i]
        for i in range(d):
            r += c(s-i, nd)
            #print(d, i, s-i, nd, c(s-i, nd))
        s -= d
        nd -= 1
    r += int(sum(digits) == old_s)  # consider n itself

    return r

def d(n):
    return sum(q(n, p) for p in primes)

#for n in range(200):
#    print(n, sum(q(n,s) for s in primes))

print(d(403539364))