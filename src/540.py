"""Brute force inclusion-exclusion. 2.5 min on laptop"""

from number import powerset, linear_sieve, linear_sieve_factors, prod

def P(N):
    lp = linear_sieve(int(N**0.5)+1)

    z = 0
    for m in range(1, int(N**0.5)+1):
        nmax = int((N - m**2)**0.5)

        if m % 2: nmax //= 2

        ps = list(powerset(linear_sieve_factors(lp, m).keys()))
        s = 0 
        # inclusion-exclusion
        for factors in ps:
            s += (-1)**len(factors) * (nmax // prod(factors))
        z += s
        
    return z // 2

print(P(3141592653589793))
