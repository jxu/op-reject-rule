# Nice sublinear problem.
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


CUTOFF = 10**7  # seems to work better than 10**8
totrange = totient_range(CUTOFF)
totsum_small = list(accumulate(totrange))

@cache
def totient_sum(n):
    """Follows the ideas outlined in my writeup plus sieving for about O(n^2/3)

    https://math.stackexchange.com/a/1740370
    """
    if n <= CUTOFF:
        return totsum_small[n]

    s = n * (n + 1) // 2
    c = int(n ** 0.5)  # works better than n^1/3

    for m in range(2, c + 1):
        s -= totient_sum(n // m)

    for k in range(1, n//c):
        s -= ((n//k) - (n//(k+1))) * totient_sum(k)

    return s


def G(N):
    s = 0
    # Largest totient calc first for value re-use (see implementation)
    current_totient_sum = totient_sum(N)

    for k in range(1, int(N**0.5)+1):
        next_totient_sum = totient_sum(N//(k+1))
        s += (k*(k+1)//2) * (current_totient_sum - next_totient_sum)
        current_totient_sum = next_totient_sum

    phi = totient_range(int(N**0.5))
    # Handle possible overlap between cases
    max_j = int(N**0.5) + (int(N**0.5) != N // int(N**0.5))
    for j in range(1, max_j):
        s += (N//j)*(N//j + 1) * phi[j] // 2

    return s

def test_totient_sum():
    # A064018
    assert totient_sum(10**9) == 303963551173008414
    assert totient_sum(10**11) == 3039635509283386211140
    print(totient_sum.cache_info())

print(G(10**11) % 998244353)
