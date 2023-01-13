# Denominator of Bernoulli numbers B_n by Bernoulli's Formula
# D(n) = product of all p such that (p-1)|n by von Staudt-Clausen theorem
# 20010 = 2*3*5*23*29, factor base = 2*2*7*11
from number import sieve, prod
from itertools import chain, combinations
from number import is_prime  # Or gmpy2

MAX_TEST = 10**9

primes = sieve(5*10**6)
all_F = []

def powerset(s, min_combo, max_combo):
    return chain.from_iterable(combinations(s, r) for r in range(min_combo, max_combo+1))

def F_valid(factors):
    ps = powerset(factors, 1, len(factors))
    for x in ps:
        f = prod(x) + 1
        if not f in (2, 3, 5, 23, 29) and is_prime(f, trials=10):
            return False

    return True

# Test adding one extra prime first
usable_p = []
for p in primes:
    factors = (2, 2, 7, 11, p)

    if F_valid(factors):
        all_F.append(prod(factors))
        usable_p.append(p)

print(usable_p[:20], usable_p[-1])
print(len(all_F))


for i in range(len(usable_p)):
    a = usable_p[i]
    for j in range(i, len(usable_p)):
        b = usable_p[j]
        factors = (2, 2, 7, 11, a, b)
        if prod(factors) > MAX_TEST: break

        if F_valid(factors):
            print((a, b), prod(factors))
            all_F.append(prod(factors))

            for k in range(j, len(usable_p)):
                c = usable_p[k]
                factors = (2, 2, 7, 11, a, b, c)
                if prod(factors) > MAX_TEST: break

                if F_valid(factors):
                    print((a, b, c), prod(factors))
                    all_F.append(prod(factors))


all_F.sort()
print(all_F[:100])
print(len(all_F))

print("F(10)", all_F[10-2])
print("F(10^5)", all_F[(10**5)-2])

