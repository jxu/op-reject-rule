from __future__ import division
from number import fib_list, sieve, memoize


fib = fib_list(24)
primes = sieve(fib[-1])

@memoize
def S(k, p_i=0):
    if k < 0: return 0
    if k == 0: return 1

    p = primes[p_i]
    if k == p: return p
    if p > k//2: return 0

    s = 0

    pow_p = 1
    for j in range(k//p + 1):
        s = (s + pow_p * S(k - j*p, p_i+1)) % 10**9
        pow_p = (pow_p * p) % 10**9

    return s


print(S(8))

# Prevent exceeding recursion limit by pre-calculating smaller S(k)
for k in range(1000, fib[-1], 1000):
    print(k, S(k), len(S.cache))

print(sum(S(f) for f in fib[2:]) % 10**9)
