from number import sieve, prod, icbrt, FenwickTree
from math import comb, isqrt
from itertools import accumulate

X_MAX = 10**12  # Module-wide maximum
ALPHA = 4       # tuning parameter, < x^1/6

Z = int(X_MAX ** (2 / 3) / ALPHA) + 1  # sieve interval
PRIMES = [0] + sieve(Z)  # precompute 1-indexed primes up to x^2/3 / alpha
print("sieve up to", Z)
ACBRTX = ALPHA * icbrt(X_MAX)

# Precompute phi(x, c) for small constant c, should be <= a = pi(x^1/3)
C = 7
PRIMES_C = PRIMES[1:C+1]
Q = prod(PRIMES_C)

# Phi_c sieves out first c primes, then counts
SIEVE_C = [1] * (Q + 1)
SIEVE_C[0] = 0
for p in PRIMES_C:
    for j in range(p, Q+1, p):
        SIEVE_C[j] = 0

PHI_C = list(accumulate(SIEVE_C))

# Precompute pi(x) for <= x^2/3 since those can be stored in memory
# (More efficient to get indicator array as part of the prime sieve() oh well
# a little faster than binary searching)
prime_count_ind = [0]*(Z + 1)
for p in PRIMES[1:]:
    prime_count_ind[p] = 1

PRIME_COUNT_SMALL = list(accumulate(prime_count_ind))


# special sieve of mu(n) pmin(n) for n <= x^1/3
N = ACBRTX + 1
MU_PMIN = [1] * N
MU_PMIN[0] = 0
for j in range(2, N):
    if MU_PMIN[j] == 1:
        for i in range(j, N, j):
            MU_PMIN[i] = -j if MU_PMIN[i] == 1 else -MU_PMIN[i]

for j in range(2, N):
    if MU_PMIN[j] == -j:
        for i in range(j*j, N, j*j):
            MU_PMIN[i] = 0

MU = [0] * N
for i in range(N):
    if MU_PMIN[i] != 0:
        MU[i] = 1 if MU_PMIN[i] > 0 else -1

def phi_c(y):
    return (y // Q) * PHI_C[Q] + PHI_C[y % Q]


def prime_count(x):
    if x < 0:
        raise ValueError

    if x <= Z:
        return PRIME_COUNT_SMALL[x]

    assert ALPHA <= int(x ** (1/6))
    acbrtx = ALPHA * icbrt(x)  # alpha cbrt(x)
    z = int(x ** (2 / 3)) // ALPHA + 1
    a = PRIME_COUNT_SMALL[acbrtx]  # pi(alpha x^1/3)
    a2 = PRIME_COUNT_SMALL[isqrt(x)]  # pi(x^1/2)

    P2 = comb(a, 2) - comb(a2, 2)
    for b in range(a+1, a2+1):
        # No recursive call
        P2 += PRIME_COUNT_SMALL[x // PRIMES[b]]

    print("P2",P2)

    S0 = 0
    for n in range(1, acbrtx+1):
        # pmin(1) = +inf
        if n == 1 or abs(MU_PMIN[n]) > PRIMES[C]:
            S0 += MU[n] * phi_c(x // n)

    print("S0",S0)

    S = 0

    # sieve out first C primes
    sieve_ind = [1] * int(1.1*z)  # hacky rounding error fix
    sieve_ind[0] = 0
    for i in range(1, C+1):
        p = PRIMES[i]
        for j in range(p, len(sieve_ind), p):
            sieve_ind[j] = 0

    sieve_c = FenwickTree(sieve_ind)

    for b in range(C, a-1):
        m_min = max(acbrtx // PRIMES[b+1], PRIMES[b+1])
        for m in range(m_min+1, acbrtx+1):
            if abs(MU_PMIN[m]) > PRIMES[b+1]:
                #print(m, b, z, x // (m * PRIMES[b+1]))
                phi_b = sieve_c.sum_to(x // (m * PRIMES[b+1]))
                S += MU[m] * phi_b

        # sieve out p_(b+1)
        p = PRIMES[b+1]
        for i in range(p, len(sieve_ind), p):
            if sieve_ind[i] == 1:
                sieve_c.add_to(i, -1)
                sieve_ind[i] = 0


    return S0 - S + a - P2 - 1


def _test_prime_count():
    # A006880
    # 10^12 may cause OOM
    powers_10 = (0, 4, 25, 168, 1229, 9592, 78498, 664579, 5761455, 50847534,
                 455052511, 4118054813, 37607912018)

    for i in range(len(powers_10)):
        assert prime_count(10**i) == powers_10[i]

print(prime_count(X_MAX))

