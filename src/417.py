# 10 hours of brute force
from number import factor, sieve, lcm, memoize
from sympy.ntheory import n_order

primes = sieve(10**4)

@memoize
def ord10(n):
    return n_order(10, n)

def L(n):
    while n % 2 == 0: n //= 2
    while n % 5 == 0: n //= 5
    if n == 1: return 0

    o = 1
    for p, e in factor(n, primes).items():


    return ord10(n)

s = 0
for i in range(1, 10**1):
    print(i)
    s += L(i)

print(s)