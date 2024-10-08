from number import sieve, prod, icbrt
from functools import cache, lru_cache
from math import comb, isqrt
from itertools import accumulate

X_MAX = 10**12  # Module-wide maximum

SIEVE_MAX = 10**8  # at least x^2/3
PRIMES = sieve(SIEVE_MAX)  # precompute 0-indexed primes up to x^2/3
print("sieve up to", SIEVE_MAX)

# Precompute phi(x, c) for small constant c, should be <= a = pi(x^1/3)
C = 7
PRIMES_C = PRIMES[:C]
C = len(PRIMES_C)
Q = prod(PRIMES_C)

SIEVE_C = [1] * (Q + 1)
SIEVE_C[0] = 0
for p in PRIMES_C:
    for j in range(p, Q+1, p):
        SIEVE_C[j] = 0

PHI_C = list(accumulate(SIEVE_C))

# Precompute pi(x) for <= x^2/3 since those can be stored in memory
# (More efficient to get indicator array as part of the prime sieve() oh well
# a little faster than binary searching)
prime_count_ind = [0]*(SIEVE_MAX+1)
for p in PRIMES:
    prime_count_ind[p] = 1

# a little faster than binary search
PRIME_COUNT_SMALL = list(accumulate(prime_count_ind))


# @cache runs out of memory now... idk
def phi(y, b):
    #print("phi",y,b)
    if y < PRIMES[b - 1]:
        return 1

    assert b >= C
    if b == C:
        return (y // Q) * PHI_C[Q] + PHI_C[y % Q]

    return phi(y, b-1) - phi(y // PRIMES[b - 1], b - 1)


def prime_count(x):
    #print("pi", x)
    if x < 0:
        raise ValueError

    if x <= SIEVE_MAX:
        return PRIME_COUNT_SMALL[x]

    a = PRIME_COUNT_SMALL[icbrt(x)]  # pi(x^1/3)
    B = PRIME_COUNT_SMALL[isqrt(x)]  # pi(x^1/2)

    P2 = comb(a, 2) - comb(B, 2)
    for j in range(a+1, B+1):
        # No recursive call
        P2 += PRIME_COUNT_SMALL[x // PRIMES[j - 1]]

    return a - P2 + phi(x, a) - 1


def test_prime_count():
    # A006880
    # 10^12 may cause OOM
    powers_10 = (0, 4, 25, 168, 1229, 9592, 78498, 664579, 5761455, 50847534,
                 455052511, 4118054813)

    for i in range(len(powers_10)):
        assert prime_count(10**i) == powers_10[i]
