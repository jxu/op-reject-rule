# 0/1 knapsack problem, solved with "meet-in-the-middle" approach
# Easiest 65% difficulty ever

from __future__ import division
from number import sieve, product, powerset
from bisect import bisect_left

primes = sieve(190)
target = product(primes)**0.5

A = primes[:len(primes)//2]
B = primes[len(primes)//2:]
pA = (product(a) for a in powerset(A))
pB = sorted(product(b) for b in powerset(B))

PSR = 0
for pa in pA:
    i = bisect_left(pB, target/pa)
    PSR = max(PSR, pB[i-1] * pa)

print(PSR)
