# 0/1 knapsack problem, solved with "meet-in-the-middle" approach
# Easiest 65% difficulty ever
from math import prod
from number import sieve, powerset
from bisect import bisect_left

primes = sieve(190)
target = prod(primes) ** 0.5

def find_lt(a, x):
    return a[bisect_left(a, x) - 1]

A = primes[:len(primes)//2]
B = primes[len(primes)//2:]
pA = (prod(a) for a in powerset(A))
pB = sorted(prod(b) for b in powerset(B))

PSR = max(pa * find_lt(pB, target/pa) for pa in pA)
print(PSR % 10**16)
