"""Brute force inclusion-exclusion on Euclid's parameterization

Primitive Pythagorean triples are of the form 
a = m^2 - n^2, b = 2mn, c = m^2 + n^2 
with m, n coprime and exactly one of them is even. 
Nice optimization from thread: WLOG use even m and odd n.

With the constraint m^2 + n^2 = c <= N,
For each m, nmax = sqrt(N - m^2)
Let m have distinct prime factors p, q, ...
By inclusion-exclusion, the count of n coprime to m is 
nmax - (nmax//p) - (nmax//q) - ... + (nmax//pq) + ... 

Use a linear sieve to get distinct prime factorization for every m, 
then brute-force inclusion-exclusion on powerset of those primes.

The time complexity is about
sum 2 ^ omega(sqrt(N - m^2)) for m up to sqrt N
omega(n) = # distinct prime factors of n
Avg order of sum 2^omega(n) over [1,N] is O(log N)? A064608 
Very small mostly, something like O(log N sqrt N).
See 540mu.py for a faster solution from the thread.

Runtime: 80 s
"""

from number import powerset, linear_sieve, prod

# a little more efficient than linear_sieve_factors
def linear_sieve_primes(lp, n):
    primes = []  # simple list instead of dict/set
    while n > 1:
        if lp[n] not in primes:
            primes.append(lp[n])
        n //= lp[n]
        
    return primes


def P(N):
    lp = linear_sieve(int(N**0.5)+1)

    s = 0
    for m in range(2, int(N**0.5)+1, 2):
        nmax = int((N - m**2)**0.5)
        
        ps = powerset(linear_sieve_primes(lp, m))
        sm = 0 
        # inclusion-exclusion
        for factors in ps:
            sm += (-1)**len(factors) * (nmax // prod(factors))
        s += sm
        
    return s

#print(P(10**6))
print(P(3141592653589793))
