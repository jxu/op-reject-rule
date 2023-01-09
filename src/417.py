# By long division, period of 1/n is just mult order of 10 mod n
# Factors of 2 and 5 can be divided out without affecting period
# For a,b coprime, order 10 mod ab = lcm(order 10 mod a, order 10 mod b)
# by CRT. So we can factor n into prime powers and take the LCM of orders

# Benchmark: P51 with sympy n_order and functools memoize, factoring takes 14m
# Without factoring takes 25m
# With memo of L_ values takes 10.5m
# 3.5m using all factorizations provided by linear sieve instead of
# sympy's n_order

from number import lcm, memoize, linear_sieve, totient_range, divisors
from collections import Counter

lp = linear_sieve(10**8)
tots = totient_range(10**8)

def pp_from_lp(lp, n):
    pp = Counter()
    while n > 1:
        pp[lp[n]] += 1
        n //= lp[n]
    return pp

@memoize
def ord10(n):
    pp = pp_from_lp(lp, tots[n])
    for d in sorted(divisors(pp)):
        if pow(10, d, n) == 1:
            return d
    raise ValueError

def L(n):
    if n % 100000 == 0: print(n)
    while n % 2 == 0: n //= 2
    while n % 5 == 0: n //= 5
    if n == 1: return 0
    return L_(n)

@memoize
def L_(n):
    o = 1
    for p, e in pp_from_lp(lp, n).items():
        o = lcm(o, ord10(p**e))
    return o


print(sum(L(i) for i in range(1, 10**8)))
