
from number import fib_list, sieve, memoize
#import functools
import sys

#sys.setrecursionlimit(5000)

fib = fib_list(24)
primes = sieve(fib[-1])

@memoize
def S(k, min_p=2):
    if k < 0: return 0
    if k == 0: return 1

    s = 0
    for p in primes:
        if p < min_p: continue
        if p > k: break
        s = (s + p * S(k-p, p)) % 10**9

    return s

print(S(8))
# Prevent exceeding recursion limit by pre-calculating smaller S(k)
for k in range(100, fib[-1], 100):
    print(k, S(k), len(S.cache))

print(sum(S(f) for f in fib[2:]) % 10**9)
