# Nice sublinear problem idea.

# Totient sum calculation: Dirichlet hyperbola like methods I explain at
# https://math.stackexchange.com/a/1740370
# Basically starting with T(n) = Sum_{m=1..n} Phi(n//m), rearrange
# Phi(n) = T(n) Sum_{m=2..n} Phi(n//m)
# The observation is n//m is constant for large m, so count precisely how many
# times each k = n//m value occurs.


# First we use S(j) = sum_{i=1..j} gcd(i,j) = sum_{d|j} d * phi(j/d)
# G(N) = sum_{j=1..N} S(j)
# By observation G(N) = sum_{j=1..N} (phi(j) sum_{i=1..N//j} i)
# = sum_{j=1..N} (1/2) (N//j) (N//j + 1) phi(j)
# Again the observation is that N//j is constant for large ranges
# We have O(n^(3/4)) algo for totient sum function Phi
# for j in (N//2, N]: sum Phi(N) - Phi(N//2)
# for j in (N//3, N//2]: sum (2*3)/2 (Phi(N//2) - Phi(N//3))
# etc. up to j near sqrt(N).
# Then calculate phi directly for phi(1) to phi(sqrt(N))

from itertools import accumulate
from functools import cache
from number import totient_range

PRECOMP = 10**7  # sweet spot
tot_range = totient_range(PRECOMP)
totsum_range = list(accumulate(tot_range))

@cache
def totient_sum(n):
    if n <= PRECOMP:
        return totsum_range[n]

    c = int(n**0.5)
    s = n * (n + 1) // 2

    for m in range(2, n//c + 1):
        s -= totient_sum(n // m)

    for k in range(1, c):
        s -= (n//k - n//(k+1)) * totient_sum(k)

    return s

def test_totient_sum():
    # A064018
    assert totient_sum(100) == 3044
    assert totient_sum(10**9) == 303963551173008414
    assert totient_sum(10**11) == 3039635509283386211140

def T(n):
    return n * (n + 1) // 2

# similar implementation to totient_sum
def G(N):
    s = 0
    c = int(N**0.5)
    for j in range(1, N//c + 1):
        s += T(N // j) * tot_range[j]
    for k in range(1, c):
        s += T(k) * (totient_sum(N // k) - totient_sum(N // (k+1)))

    return s

print(G(10**11) % 998244353)
