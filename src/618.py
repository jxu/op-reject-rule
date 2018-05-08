# Using memoize decorator was slower than allocating a large lookup table

from __future__ import division
from number import fib_list, sieve, memoize
import sys

sys.setrecursionlimit(50000)


fib = fib_list(24)
primes = sieve(fib[-1])
sp = set(primes)

memo_maxk = fib[-1]
memo_maxi = len(primes)
memo = [[-1]*memo_maxi for _ in range(memo_maxk)]

#@memoize
def S(k, p_i=0):
    if k < 0 or p_i >= len(primes): return 0
    if k == 0: return 1

    if memo[k][p_i] != -1:
        return memo[k][p_i]

    p = primes[p_i]
    s = 0
    if p > k: s = 0
    elif k not in sp and 2*p > k: s = 0
        #elif 3*p > k and k-p not in sp:
        #    s = S(k, p_i+1) % 10**9

    else:
        pow_p = 1
        for j in range(k//p + 1):
            s = (s + pow_p * S(k - j*p, p_i+1)) % 10**9
            pow_p = (pow_p * p) % 10**9

    memo[k][p_i] = s
    return s

# Sanity test
assert (S(1), S(2), S(3), S(5), S(8)) == (0, 2, 3, 11, 49)

# Precompute some values of S(k)
for k in range(0, fib[-1], 100):
    print(k, S(k))

final_sum = 0
for f in fib[2:]:
    s = S(f)
    print(f, s)
    final_sum += s

print(final_sum % 10**9)

