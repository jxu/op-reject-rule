from number import sieve
from functools import cache
from sys import setrecursionlimit

primes = sieve(100000)
k = 2
N = primes[k]
S = N * primes[k-1]  # max possible sum of a_i
print(N, S)

@cache
def m(n, s):
    print(n, s)
    if n == 0:
        return 0 if s == 0 else -1e9
    if s < 0: return -1e9
    return max(m(n-1, s-a) + primes[a] for a in range(k-10, k))


memo = [-1e9]*(S+1)
memo[0] = 0

for n in range(N):
    new_memo = memo[:]
    for s in range(S+1):
        for a in range(s, k):
            new_memo[s] = max(new_memo[s], memo[s-a] + primes[a])

    memo = new_memo

print(memo)