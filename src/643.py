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
# f(N) = \sum_{odd n} (N//2n choose 2) \mu(n)
# Let M*(n) be the odd Mertens function, defined by
# M*(n) = \sum \mu(k) for odd k, 1 <= k <= n.
# Let r be an odd number. Since mu(r) is multiplicative,
# mu(2r) = -mu(r) and mu(4r) = mu(8r) = ... = 0.
#
# So splitting M(n) = \sum_{k=1}^n mu(k), the standard Mertens function, by
# even and odd k, we only need to consider odd k and even k not divisible by 4.
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

from itertools import accumulate
from number import sieve
from math import comb
from functools import cache

def mobius_range(n, primes):
    """Computes Möbius function for 0 to n using sieve approach.

    Requires `primes` to contain all primes below n.
    https://mathoverflow.net/a/200392
    """
    mus = [1] * (n+1)
    mus[0] = 0
    for p in primes:
        if p > n: break
        for i in range(p, n+1, p):
            mus[i] *= -1
        for i in range(p**2, n+1, p**2):
            mus[i] = 0

    return mus

mertens_large = dict()
mertens_small = None
mertens_small_cutoff = -1

def mertens(n, primes):
    """Calculates Mertens function M(n), aka Möbius summatory function

    Very similar approach to totient sum.
    `primes` must contain primes up to cutoff value n^(2/3)
    https://mathoverflow.net/a/320042
    """
    assert n >= 1
    cutoff = int(n**(2/3))
    global mertens_small_cutoff

    if cutoff > mertens_small_cutoff:
        mertens_small_cutoff = cutoff
        mobius_small = mobius_range(cutoff, primes)
        global mertens_small
        mertens_small = list(accumulate(mobius_small))


    def M(n):
        if n < cutoff:
            global mertens_small
            return mertens_small[n]

        if n in mertens_large:
            return mertens_large[n]

        isqrtn = int(n**0.5)
        s = 1
        for x in range(2, isqrtn+1):
            s -= M(n // x)

        for y in range(1, isqrtn + (isqrtn != n // isqrtn)):
            s -= (n//y - n//(y+1)) * M(y)

        mertens_large[n] = s
        return s

    return M(n)

N = 10**11

primes = sieve(10**8)
small_mobius = mobius_range(int(N**0.5), primes)



def test_mobius_range():
    # A008683
    small_mus = [0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1,0,-1,0,-1,
                 0,1,1,-1,0,0,1,0,0,-1,-1]
    n = len(small_mus)-1
    primes = sieve(n)

    assert mobius_range(n, primes) == small_mus

def test_mertens_pow10():
    primes = sieve(10 ** 5)
    # A084237
    powers_10 = (1, -1, 1, 2, -23, -48, 212, 1037)
    for i in range(1, len(powers_10)):
        assert mertens(10 ** i, primes) == powers_10[i]



def test_mertens_small():
    primes = sieve(10)
    # A002321
    mertens_small_ = (0,1,0,-1,-1,-2,-1,-2,-2,-2,-1,-2,
                      -2,-3,-2,-1,-1,-2,-2,-3,-3)
    for i in range(1, len(mertens_small_)):
        assert mertens(i, primes) == mertens_small_[i]

@cache
def odd_mertens(n):
    # May save computation to use small_mobius to calculate small odd_mertens
    if n < 1: return 0
    return mertens(n, primes) + odd_mertens(n//2)


result = 0
last_binom = 0
for k in range(1, int(N**0.5), 2):
    result += comb(N // (2 * k), 2) * small_mobius[k]
    last_binom = N // (2*k)

for j in range(1, last_binom):
    mu_sum = odd_mertens(N//(2*j)) - odd_mertens(N//(2*(j+1)))
    result += comb(j, 2) * mu_sum

print(result)
print(result % 1000000007)
