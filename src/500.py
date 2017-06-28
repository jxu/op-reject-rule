# Ref: A037992. For n = p1^a1...p1^ak, d(n) = (1 + a1)...(1 + ak)
# Write 1 + ai = 2^mi, m1 + m2 + ... + mk = 500500
# Store all mi as array m. If the answer is smallest num with 2^x divisors, it
# turns out the array m for 2^x is the array with 2^(x-1) with 1 added to some
# mi. So we find the mi that increases log(answer) the least.
# 10 minutes with pypy :(

from number import sieve
from math import log

LIMIT = 500500
primes = sieve(10**7)[:LIMIT]


m = [0]*LIMIT

for i in range(LIMIT):
    min_to_add = float("inf")
    best_j = None

    for j in range(LIMIT):
        # Don't increase m[j] if m[j-1] == m[j]
        if j == 0 or m[j] != m[j-1]:
            # Test m[j] += 1
            new_to_add = 2**m[j] * log(primes[j])

            #print(i, j, m, new_to_add, min_to_add)
            if new_to_add < min_to_add:
                min_to_add = new_to_add
                best_j = j

    m[best_j] += 1


answer = 1
for i in range(LIMIT):
    answer = (answer * pow(primes[i], 2**m[i] - 1, 500500507)) % 500500507
print(answer)

