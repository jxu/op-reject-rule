# Denominator of Bernoulli numbers B_n by Bernoulli's Formula
# D(n) = product of all p such that (p-1)|n by von Staudt-Clausen theorem
# 20010 = 2*3*5*23*29, factor base = 2*2*7*11
from number import sieve, product
from itertools import chain, combinations
from gmpy2 import is_prime

MAX_EXTRA_PRIMES = 5
MAX_TEST = 10**10

primes = sieve(10**7)
sp = set(primes)
all_F = []

def powerset(s, min_combo, max_combo):
    return chain.from_iterable(combinations(s, r) for r in range(min_combo, max_combo+1))

def F_valid(ps):
    for x in ps:
        f = product(x)+1
        if is_prime(f) and not f in (2, 3, 5, 23, 29):
            return False

    return True

# Test adding one extra prime first
usable_p = []
for p in primes:
    if p > 5*10**6: break
    factors = [2, 2, 7, 11, p]
    ps = powerset(factors, 0, len(factors))

    if F_valid(ps):
        all_F.append(product(factors))
        usable_p.append(p)

print(usable_p[:20], usable_p[-1])
#all_F = list(set(all_F))
print(len(all_F))


for i in range(len(usable_p)):
    for j in range(i, len(usable_p)):
        a = usable_p[i]
        b = usable_p[j]
        factors = [2, 2, 7, 11, a, b]
        if product(factors) > 2*2*7*11*usable_p[-1]: break

        ps = powerset(factors, 0, len(factors))
        if F_valid(ps):
            print((a, b), product(factors))
            all_F.append(product(factors))


for i in range(len(usable_p)):
    a = usable_p[i]

    for j in range(i, len(usable_p)):
        b = usable_p[j]
        if 2*2*7*11*a*b > usable_p[-1]: break

        for k in range(j, len(usable_p)):
            c = usable_p[k]
            factors = [2, 2, 7, 11, a, b, c]
            if product(factors) > 2*2*7*11*usable_p[-1]: break

            ps = powerset(factors, 0, len(factors))
            if F_valid(ps):
                print((a, b, c), product(factors))
                all_F.append(product(factors))

all_F = list(set(all_F))
all_F.sort()
print(all_F[:100])
print(len(all_F))

print("F(10)", all_F[10-2])
print("F(10^5)", all_F[(10**5)-2])


