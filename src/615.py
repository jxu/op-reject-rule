# Let M = 10^6. Smallest num with 1 million prime factors: 2^M
# Upper bound: 2^(M-1) * p_M, with p_M about 1.55e7
from __future__ import division
from number import sieve

# Parameters to tune
DEPTH = 10
MAX_NUM = 10**10
M = 10**6
PRIMES = sieve(10**6)
MAX_I = len(PRIMES)

l = []

def build(product, depth, min_i):

    if depth >= DEPTH:
        l.append(product)

    for i in range(min_i, MAX_I):
        if product * PRIMES[i] >= MAX_NUM: break
        build(product*PRIMES[i], depth+1, i)


build(1, 0, 0)
print(len(l))
n = sorted(l)[M-1]

print(n, n/(2**DEPTH))
print((pow(2, M - DEPTH, 123454321) * n) % 123454321)