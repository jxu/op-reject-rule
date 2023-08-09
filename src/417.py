# By long division, period of 1/n is just mult order of 10 mod n
# Factors of 2 and 5 can be divided out without affecting period
# For a,b coprime, order 10 mod ab = lcm(order 10 mod a, order 10 mod b)
# by CRT. So we can factor n into prime powers and take the LCM of orders
# TODO: explain L(p^k) optimization

# Benchmark: P51 with sympy n_order and functools memoize, factoring takes 14m
# Without factoring takes 25m
# With memo of L_ values takes 10.5m
# 2.5m using all factorizations provided by linear sieve instead of
# sympy's n_order

from number import memoize, linear_sieve, divisors, \
    factors_from_linear_sieve
from math import lcm

lp = linear_sieve(10**8)

@memoize
def ord10(p, e):
    if e == 1:
        pp = factors_from_linear_sieve(lp, p-1)
        for d in sorted(divisors(pp)):
            if pow(10, d, p) == 1:
                return d
        raise ValueError

    le = ord10(p, e-1)
    return le if pow(10, le, p**e) == 1 else p * le

def L(n):
    if n % 100000 == 0: print(n)
    while n % 2 == 0: n //= 2
    while n % 5 == 0: n //= 5
    if n == 1: return 0
    return L_(n)

@memoize
def L_(n):
    if n == 1: return 1
    m = n
    p = lp[n]
    #print(n, p)
    e = 0
    while m % p == 0:
        m //= p
        e += 1

    return lcm(L_(m), ord10(p, e))


print(sum(L(i) for i in range(1, 10**8)))
print(ord10.cache_info())
print(L_.cache_info())