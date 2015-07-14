# Closest would be "very prime" number (but not prime itself)
# Use semi-primes
from number import phi, sieve
import time

start = time.process_time()

primes = sieve(10**4)
min_r = 2
min_n = 0
for p_i in range(len(primes)):
    p = primes[p_i]
    for q_i in range(p_i+1, len(primes)):
        q = primes[q_i]
        n = p*q

        if n >= 10**7: break

        t = phi(n)
        if sorted(str(t)) == sorted(str(n)):
            if n/t < min_r:
                min_r = n/t
                min_n = n
                print(n, t, n/t)

print(min_n)
print(time.process_time() - start)