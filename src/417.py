# By long division, period of 1/n is just mult order of 10 mod n. A051626
# Factors of 2 and 5 can be divided out without affecting period
# For a,b coprime, order 10 mod ab = lcm(order 10 mod a, order 10 mod b)
# by CRT. So we can factor n into prime powers and take the LCM of orders
# TODO: explain L(p^k) optimization

# Benchmark: P51 with sympy n_order and functools memoize, factoring takes 14m
# Without factoring takes 25m
# With memo of L_ values takes 10.5m
# 2.5m using all factorizations provided by linear sieve instead of n_order
# 2m with optimizations to lcm and ord10 calc
# 1.5m replacing memoize with DP array
# 30s with sympy's order algorithm
# 25s with mul order algorithm from Bach & Shallit
#   https://rosettacode.org/wiki/Multiplicative_order

from number import linear_sieve, linear_sieve_factors
from math import lcm

lp = linear_sieve(10**8)
L = [0] * (10**8 + 1)

def mul_order(a, n, phi_n=None, factors_phi=None):
    order = 1
    for qi, ei in factors_phi.items():
        yi = phi_n // (qi ** ei)
        xi = pow(a, yi, n)
        while xi != 1:
            xi = pow(xi, qi, n)
            order *= qi

    return order

for n in range(2, 10**8 + 1):  # DP
    m = n
    if n % 100000 == 0: print(n)
    # try to factor out 2 and 5
    while m % 2 == 0: m //= 2
    while m % 5 == 0: m //= 5
    if m < n:
        L[n] = L[m]
        continue

    # factor out smallest prime power
    p = lp[n]
    m, pp = n, 1

    while m % p == 0:
        m //= p
        pp *= p

    if n == pp:  # n prime power, so actually calculate order
        if n == p:
            L[n] = mul_order(10, p, p - 1, linear_sieve_factors(lp, p - 1))

        else:
            le = L[n // p]
            L[n] = le if pow(10, le, n) == 1 else p * le
    else:
        L[n] = lcm(L[m], L[pp])  # CRT

print(sum(L))
