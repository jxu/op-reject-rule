# Nice sublinear problem idea.

# Totient sum calculation: Dirichlet hyperbola like methods I explain at
# https://math.stackexchange.com/a/1740370
# Basically starting with T(n) = Sum_{i=1..n} Phi(n//i), rearrange
# Phi(n) = T(n) Sum_{i=2..n} Phi(n//i)
# The observation is n//i is constant for large i, so count precisely how many
# times each j = n//i value occurs.

# gcdsum(j) = Sum_{i=1..j} gcd(i, j) = Sum_{d|j} d * phi(j/d)
# because d = gcd(i, j) exactly when d|i and d|j and gcd(i/d, j/d) = 1
# so there are phi(j/d) terms of d
# As gcdsum = Id (Dirichlet convolution) phi
# f = Id, g = phi, summatory functions F = T, G = Phi
# Apply the O(n^3/4) Dirichlet hyperbola method directly to gcdsum:
# Sum_{j=1..n} gcdsum(j) =
# Sum_{i<=sqrt n} f(i) G(n/i) + Sum_{j<=sqrt n} g(j) F(n/j)
# - F(sqrt n) * G(sqrt n)

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

    c = int(n**0.5)  # can adjust but sqrt n seems to work the best
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

# use hyperbola method instead of floor counting
# totients and totient sums calculated before
def G(N):
    s = 0
    isqrt = int(N**0.5)  # fixed
    for i in range(1, isqrt+1):
        s += i * totient_sum(N // i)

    for j in range(1, isqrt+1):
        s += tot_range[j] * T(N // j)

    s -= T(isqrt) * totient_sum(isqrt)

    return s

print(G(10**11) % 998244353)
