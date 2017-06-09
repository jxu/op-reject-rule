from __future__ import division
from number import sieve, prime_count

def f(n):
    primes = sieve(int(n**0.5))

    # Case 1: n = p^7
    count = prime_count(int(n**(1/7)))

    # Case 2: n = p^3 * q
    for p in primes:
        if p**3 > n: break
        q_max = n // (p**3)
        # Exclude case with p == q
        count += prime_count(q_max) - (q_max >= p)

    # Case 3: n = p*q*r, p < q < r
    for p_i in range(len(primes)):
        p = primes[p_i]
        if p**3 > n: break

        for q_i in range(p_i + 1, len(primes)):
            q = primes[q_i]
            if q > (n / p)**0.5: break  # max q when q = r so n = p * q^2
            print(p, q)
            # q < r < n/pq, so add pi(n/pq) - pi(q)
            count += prime_count(n // (p*q)) - (q_i + 1)

    return count


print(f(10**12))