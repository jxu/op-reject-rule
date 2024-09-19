"""Pengolodh (et al.) idea: use Möbius function for inclusion-exclusion

Same parameterization. C(N) counts lattice points (odd m, even n) within sqrt N
from origin; i.e. m^2 + n^2 <= N. 

P(N) uses mu(d) over odd d to perfom inclusion-exclusion over common divisor d
of m,n. (2 is already not a common factor from odd m)
C(N / d^2) counts lattice points that have coord multiples of d.
(dm)^2 + (dn)^2 <= N  <=>  m^2 + n^2 <= N / d^2 

The resulting code, with mobius_range already implemented, is quite short.

Time complexity: about sum sqrt(N/d^2) from 1 to sqrt(N) 
= O(sqrt(N) log(N)), same as original? 
Runtime: 16 s 
"""
from number import mobius_range

def C(N):
    return sum(int((N - m**2)**0.5) // 2 
               for m in range(1, int(N**0.5)+1, 2))


def P(N): 
    mu = mobius_range(int(N**0.5))
     
    return sum(mu[d] * C(N / (d**2)) 
               for d in range(1, int(N**0.5)+1, 2))

#print(P(10**6))
print(P(3141592653589793))
