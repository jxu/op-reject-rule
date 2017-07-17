# Brute force, combine together all primes with unique digits

from itertools import permutations
from number import is_prime

primes = []
prime_digits = []
for l in range(1, 10):
    for perm in permutations(range(1, 10), l):
        p = 0
        for x in perm: p = 10*p + x
        if is_prime(p):
            primes.append(p)
            prime_digits.append(perm)

prime_sets = 0

# pool is an array of bools, with pool[d] representing if d has been used
def create_set(i, pool):
    if all(pool):
        global prime_sets
        prime_sets += 1

    digits_left = pool.count(False)

    for j in range(i+1, len(primes)):
        if len(prime_digits[j]) > digits_left: break

        if not any(pool[d] for d in prime_digits[j]):
            for d in prime_digits[j]: pool[d] = True
            create_set(j, pool)
            for d in prime_digits[j]: pool[d] = False


create_set(-1, [True] + [False]*9)
print(prime_sets)