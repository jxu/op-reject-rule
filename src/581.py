# Consecutive pairs of smooth numbers are given by Størmer's theorem
# Procedure given by Lehmer. May also be A002071?

# Solving x^2 - 2qy^2 = 1, where q could be product of primes below 47
# (614889782588491410?)

# Testing out SymPy's Pell equation solver.
# Implement own solver? http://docs.sympy.org/dev/_modules/sympy/solvers/diophantine.html#diop_DN
# Faster with python3 instead of pypy??

from sympy.solvers.diophantine import diop_DN
from number import sieve, powerset, product


def p_smooth_tri(p):
    primes = sieve(p+1)
    for prime_combo in powerset(primes):
        q = product(prime_combo)
        if q == 2: continue
        print(diop_DN(2*q, 1))


p_smooth_tri(20)