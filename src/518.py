# divisibility method of a from dev_random:
# let a', b', c' = a+1, b+1, c+1
# geometric sequence b' = a'k/d, c' = a'k^2/d^2 for coprime k,d
# so d^2 divides a', search a' as multiples of squares
# P51 pypy3.6 benchmark: 37s
from number import sieve
from math import gcd

def S(n):
    s = 0
    sp = set(sieve(n))

    for d in range(1, n):
        for a1 in range(d**2, n, d**2):
            a = a1 - 1
            if a not in sp: continue
            for k in range(d+1, n):
                b1 = a1 // d * k
                c1 = b1 // d * k
                if c1 > n: break
                if gcd(d, k) > 1: continue
                b, c = b1 - 1, c1 - 1
                if b in sp and c in sp:
                    print(f"{k}/{d}", a, b, c)
                    s += a + b + c

    return s

print(S(10**8))
