# Basic recurrence, considering up to ith prime:
# S(k, i) = S(k, i-1) + p_i * S(k - p_i, i)
# Requires O(k pi(k)) space, where k = F_24 ≈ 50000, pi(k) ≈ 5000
# Simple space optimization: let level i overwrite level i-1 as k increases
from number import fib_list, sieve

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
