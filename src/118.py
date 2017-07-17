# Brute force

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

print(prime_digits[:20])
print(primes[:100])
print(len(primes))


prime_sets = 0

# pool is an array of bools, with pool[d] representing if d has been used
def create_set(i, pool, s):
    if all(pool):
        print(s)
        global prime_sets
        prime_sets += 1
    #print(i, pool, s)

    digits_left = pool.count(False)
   # print(i, pool, s, digits_left)

    for j in range(i+1, len(primes)):
        if len(prime_digits[j]) > digits_left: break

        if not any(pool[d] for d in prime_digits[j]):
            for d in prime_digits[j]: pool[d] = True
            create_set(j, pool, s + [primes[j]])
            for d in prime_digits[j]: pool[d] = False


create_set(-1, [True]+[False]*9, [])
print(prime_sets)