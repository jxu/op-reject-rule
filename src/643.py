"""
New solution
------------
For each fixed t, gcd(a, b) = 2^t <=> gcd(a/2^t, b/2^t) = 1 
So for each b (div by 2^t), the # a's satisfying is phi(b/2^t)
For a < b <= N, this is summatory function Phi(b / 2^t)
The exception is when b/2^t = 1, where we want phi(1) = 0 instead of 1 

Old solution
------------
What a journey. I did not use totient function at all, instead I directly
counted the pairs by inclusion-exclusion.

A pair of numbers is counted in the sum iff it has a common factor of 2 and
no other prime. Let $O$ be the odd primes. Then the sum is
f(N) = (N//2 choose 2)
- \sum_{p \in O} (N//2p choose 2)
+ \sum_{(p,q) \in (O choose 2)} (N//2pq choose 2)
- \sum_{(p,q,r) \in (O choose 3)} (N//2pqr choose 2) + ...

This is exactly
f(N) = \sum_{odd n} (N//2n choose 2) \mu(n)
Let M*(n) be the odd Mertens function, defined by
M*(n) = \sum \mu(k) for odd k, 1 <= k <= n.
Let r be an odd number. Since mu(r) is multiplicative,
mu(2r) = -mu(r) and mu(4r) = mu(8r) = ... = 0.

So splitting M(n) = \sum_{k=1}^n mu(k), the standard Mertens function, by
even and odd k, we only need to consider odd k and even k not divisible by 4.
This gives the identity M(n) = M*(n) - M*(n/2) or equivalently
M*(n) = M(n) + M*(n/2), so with a sublinear algorithm to calculate the
Mertens function we have our odd Mertens function too.

Then we split the summation based on sqrt n to get the final formula
f(N) = \sum_{odd n}^{\sqrt N} (N//2n choose 2) mu(n) +
\sum_{j=1}^{jmax-1} (j choose 2) g(j)
with g(j) = \sum_{N//2j = k} mu(k) to account fully for the
inclusion-exclusion.

g(j) = M*(N//2j) - M*(N//2(j+1)) and jmax is the smallest value of
N//2n we've already accounted for.

The inefficiency with this solution is computing M*(n) recursively.
"""

from functools import cache
from number import totient_range, totient_sum, totient_sum_range

PRECOMP = 10**7  # sweet spot
tot_range = totient_range(10**7)
totient_sum.totsum_range = totient_sum_range(tot_range)

N = 10**11

s = 0
p2 = 2 
while p2 <= N:
    s += totient_sum(N // p2) - 1 
    p2 *= 2
    
print(s % 1000000007)
