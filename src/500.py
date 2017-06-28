# Ref: A037992

from number import sieve
from math import log

LIMIT = 500

primes = sieve(10**5)[:LIMIT]

def log_num(m):
    s = 0
    for i in range(len(m)):
        if m[i] == 0: break  # m must be decreasing for early break to work
        s += (2**m[i] - 1) * log(primes[i])
    return s


m = [0]*LIMIT
for i in range(LIMIT):
    #print(m)
    min_num = float("inf")
    best_j = None

    for j in range(LIMIT):
        # Don't increase m[j] if m[j-1] == m[j]
        if j == 0 or m[j] != m[j-1]:
            m[j] += 1
            new_num = log_num(m)
            #print(i, j, m, new_num, min_num)
            if new_num < min_num:
                min_num = new_num
                best_j = j
            m[j] -= 1

    m[best_j] += 1


answer = 1
for i in range(LIMIT):
    answer = (answer * pow(primes[i], 2**m[i] - 1, 500500507)) % 500500507
print(answer)
