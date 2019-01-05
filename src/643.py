# What a journey. I did not use totient function at all, instead I directly
# counted the pairs by inclusion-exclusion.
#
# A pair of numbers is counted in the sum iff it has a common factor of 2 and
# no other prime. Let $O$ be the odd primes. Then the sum is
# f(N) = (N//2 choose 2)
# - \sum_{p \in O} (N//2p choose 2)
# + \sum_{(p,q) \in (O choose 2)} (N//2pq choose 2)
# - \sum_{(p,q,r) \in (O choose 3)} (N//2pqr choose 2) + ...
#
# This is exactly
# f(N) = \sum_{odd n} (N//2n choose 2) \mu(n)$$
# Let M*(n) be the odd Mertens function, defined by
# M*(n) = \sum \mu(k) for odd k, 1 <= k <= n.
# Let r be an odd number. Since mu(r) is multiplicative,
# mu(2r) = -mu(r) and mu(4r) = mu(8r) = ... = 0.
#
# So splitting M(n), the standard Mertens function, by even and odd n,
# we only need to consider odd n and even n not divisible by 4.
# This gives the identity M(n) = M*(n) - M*(n/2) or equivalently
# M*(n) = M(n) + M*(n/2), so with a sublinear algorithm to calculate the
# Mertens function we have our odd Mertens function too.
#
# Then we split the summation based on sqrt n to get the final formula
# f(N) = \sum_{odd n}^{\sqrt N} (N//2n choose 2) mu(n) +
# \sum_{j=1}^{jmax-1} (j choose 2) g(j)
# with g(j) = \sum_{N//2j = k} mu(k) to account fully for the
# inclusion-exclusion.
#
# g(j) = M*(N//2j) - M*(N//2(j+1)) and jmax is the smallest value of
# N//2n we've already accounted for.
#
# The inefficiency with this solution is computing M*(n) recursively.

from __future__ import division
from number import sieve, combination, mobius_range, mertens, memoize
N = 10**11

primes = sieve(10**8)
small_mobius = mobius_range(int(N**0.5), primes)

@memoize
def odd_mertens(n):
    if n < 1: return 0
    return mertens(n, primes) + odd_mertens(n//2)


result = 0
last_binom = 0
for k in range(1, int(N**0.5), 2):
    result += combination(N // (2*k), 2) * small_mobius[k]
    last_binom = N // (2*k)

for j in range(1, last_binom):
    mu_sum = odd_mertens(N//(2*j)) - odd_mertens(N//(2*(j+1)))
    result += combination(j, 2) * mu_sum

print(result)
print(result % 1000000007)