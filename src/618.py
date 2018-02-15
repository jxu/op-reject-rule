from __future__ import division
from number import fib_list, sieve, memoize


fib = fib_list(24)
primes = sieve(fib[-1])
sp = set(primes)

@memoize
def S(k, p_i=0):
    if k < 0: return 0
    if k == 0: return 1

    p = primes[p_i]
    if p > k: return 0
    if k not in sp:
        if 2*p > k: return 0
        if 3*p > k and k-p not in sp:
            return S(k, p_i+1) % 10**9

    s = 0

    pow_p = 1
    for j in range(k//p + 1):
        s = (s + pow_p * S(k - j*p, p_i+1)) % 10**9
        pow_p = (pow_p * p) % 10**9

    return s

print(S(1), S(2), S(3), S(5), S(8))
assert (S(1), S(2), S(3), S(5), S(8)) == (0, 2, 3, 11, 49)

# Prevent exceeding recursion limit by pre-calculating smaller S(k)
for k in range(1000, fib[-1], 1000):
    print(k, S(k), len(S.cache))
    if k == 1000: assert(S(k) == 542144285)


print(sum(S(f) for f in fib[2:]) % 10**9)
