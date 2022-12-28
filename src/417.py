# By long division, period of 1/n is just mult order of 10 mod n
# Factors of 2 and 5 can be divided out without affecting period
# For a,b coprime, order 10 mod ab = lcm(order 10 mod a, order 10 mod b)
# by CRT. So we can factor n into prime powers and take the LCM of orders

# Benchmark: P51 with sympy n_order and functools memoize, factoring takes 14m
# Without factoring takes 25m
from number import factor, sieve, lcm, memoize
from sympy.ntheory import n_order

primes = sieve(10**4)

@memoize
def ord10(n):
    return n_order(10, n)

def L(n):
    if n % 10000 == 0: print(n)
    while n % 2 == 0: n //= 2
    while n % 5 == 0: n //= 5
    if n == 1: return 0

    o = 1
    for p, e in factor(n, primes).items():
        o = lcm(o, ord10(p**e))

    return o

print(sum(L(i) for i in range(1, 10**8)))
