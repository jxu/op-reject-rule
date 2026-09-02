# Much faster (0.5 s) iterative version that overwrites DP array
# based on Robert_OConnor's solution

from number import fib_list, sieve
import sys

fib = fib_list(24)
primes = sieve(fib[-1])

def S(k):
    m = [1] + [0] * fib[-1]
    for p in primes:
        for j in range(p, k+1):
            m[j] = (m[j] + p * m[j-p]) % 10**9
    return m

m = S(fib[-1])
print(sum(m[fib[i]] for i in range(2, 25)) % 10**9)
