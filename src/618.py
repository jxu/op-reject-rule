# Simple DP (F_24 ~ 50000, about 5000 primes below F_24)
# Recursion runs out of stack memory using Python 3.6.
# Runs fine in about 1.5 mins with Pypy 2.7 and 3.6

# (also A002098) G.f. approach is
# Product_p ((p x^p)^0 + (p x^p)^1 + (p x^p)^2 + ...)
# = Product_p 1 / (1 - p x^p)

from number import fib_list, sieve, memoize
import sys
sys.setrecursionlimit(30000)

fib = fib_list(24)
primes = sieve(fib[-1])

@memoize
def S(k, i=len(primes)-1):
    if k < 0 or i < 0: return 0
    if k == 0: return 1
    return (S(k, i-1) + primes[i] * S(k - primes[i], i)) % 10**9

#print(sum(S(fib[i]) for i in range(2, 25)) % 10**9)

# Much faster (0.5 s) iterative version that overwrites DP array
# based on Robert_OConnor's solution
def S2(k):
    m = [1] + [0] * fib[-1]
    for p in primes:
        for j in range(p, k+1):
            m[j] = (m[j] + p * m[j-p]) % 10**9
    return m

m = S2(fib[-1])
print(sum(m[fib[i]] for i in range(2, 25)) % 10**9)
