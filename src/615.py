# Let M = 10^6. Smallest num with 1 million prime factors: 2^M
# Upper bounds: 2^(M-1) * M,
# 2^(M-1)*n with n having at least 1 prime factor,
# 2^(M-2)*n with n having at least 2 prime factors,
# ... for 2^(M-4)*n with n having 4 or more prime factors. There are ~M such
# n below 2.11e6.
from __future__ import division
from number import sieve
import heapq

# Parameters to tune
DEPTH = 22
max_num = 10**12
M = 10**6
PRIMES = sieve(10**7)
MAX_I = len(PRIMES)

h = []

def build(product, depth, min_i):

    if depth >= DEPTH:
        heapq.heappush(h, product)
        if len(h) >= M and len(h) % 10**4 == 0:
            global max_num
            max_num = min(max_num, h[M-1])
            print(len(h), max_num, max_num/(2**DEPTH))

    for i in range(min_i, MAX_I):
        if product * PRIMES[i] >= max_num: break
        build(product*PRIMES[i], depth+1, i)


build(1, 0, 0)
n = h[M-1]

print(n, n/(2**DEPTH), len(h))
print((pow(2, M - DEPTH, 123454321) * n) % 123454321)