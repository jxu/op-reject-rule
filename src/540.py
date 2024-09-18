"""Brute force inclusion-exclusion. 2.5 min on laptop"""

from number import powerset, linear_sieve, linear_sieve_factors, prod

# a little more efficient than linear_sieve_factors
def linear_sieve_distinct_factors(lp, n):
    primes = []  # simple list instead of dict/set
    while n > 1:
        if lp[n] not in primes:
            primes.append(lp[n])
        n //= lp[n]
        
    return primes


def P(N):
    lp = linear_sieve(int(N**0.5)+1)

    z = 0
    for m in range(1, int(N**0.5)+1):
        nmax = int((N - m**2)**0.5)
        if m % 2: nmax //= 2  # m odd => n even

        ps = powerset(linear_sieve_distinct_factors(lp, m))
        s = 0 
        # inclusion-exclusion
        for factors in ps:
            s += (-1)**len(factors) * (nmax // prod(factors))
        z += s
        
    return z // 2  # symmetry for n < m

print(P(3141592653589793))
