# Let M = 10^6. Smallest num with 1 million prime factors: 2^M
# Upper bound: 2^(M-1) * p_M, with p_M about 1.55e7
from __future__ import division
from number import sieve
import heapq

# Parameters to tune
DEPTH = 9
max_num = 10**11
M = 10**6
PRIMES = sieve(10**7)
MAX_I = len(PRIMES)

h = []

def build(product, depth, min_i):

    if depth >= DEPTH:
        heapq.heappush(h, product)
        if len(h) >= M and len(h) % 10**6 == 0:
            global max_num
            max_num = min(max_num, h[M-1])
            print(len(h), max_num)

    for i in range(min_i, MAX_I):
        if product * PRIMES[i] >= max_num: break
        build(product*PRIMES[i], depth+1, i)


build(1, 0, 0)
n = h[M-1]

print(n, n/(2**DEPTH), len(h))
print((pow(2, M - DEPTH, 123454321) * n) % 123454321)