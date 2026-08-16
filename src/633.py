# See 633.md for explanation
from number import sieve
from functools import cache 
from math import pi

primes = sieve(10**6)

@cache
def p(k):
    return sum((q**2 - 1)**-k for q in primes)

@cache
def e(k):
    if k == 0: return 1
    return sum((-1)**(j-1) * e(k-j) * p(j) for j in range(1, k+1)) / k

print(f"{(6 / (pi**2)) * e(7):.4e}")
