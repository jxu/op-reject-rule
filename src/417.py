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

from number import linear_sieve, divisors, factors_from_linear_sieve
from math import lcm

lp = linear_sieve(10**8)
L = [0] * (10**8 + 1)


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
            pp = factors_from_linear_sieve(lp, p - 1)
            for d in sorted(divisors(pp)):
                #print(n, d)
                if pow(10, d, p) == 1:
                    L[n] = d
                    break
        else:
            le = L[n // p]
            L[n] = le if pow(10, le, n) == 1 else p * le
    else:
        L[n] = lcm(L[m], L[pp])

#print(L[:20])
print(sum(L))
