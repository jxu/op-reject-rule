from number import sieve, prod, FenwickTree
from math import comb, isqrt
from itertools import accumulate

X_MAX = 10**12  # Module-wide maximum
ALPHA = 10      # tuning parameter, < x^1/6
C = 7           # precompute phi(x,c)

Z = (X_MAX)**(2/3) / ALPHA  # sieve max, doesn't need to be exact
PRIMES = [0] + sieve(int(Z)+1)  # precompute 1-indexed primes up to z
print("sieve up to", int(Z)+1)


ACBRTX = int(ALPHA * X_MAX**(1/3)) + 1  # not exact
assert C <= ACBRTX
PRIMES_C = PRIMES[1:C+1]
Q = prod(PRIMES_C)

# Phi_c sieves out first c primes
SIEVE_C = [1] * (Q + 1)
SIEVE_C[0] = 0
for p in PRIMES_C:
    for j in range(p, Q+1, p):
        SIEVE_C[j] = 0

PHI_C = list(accumulate(SIEVE_C))

# Precompute pi(x) for <= z ~ x^2/3 since those can be stored in memory
# (More efficient to get indicator array as part of the prime sieve() oh well
# a little faster than binary searching)
prime_count_ind = [0]*int(Z + 1)
for p in PRIMES[1:]:
    prime_count_ind[p] = 1

PRIME_COUNT_SMALL = list(accumulate(prime_count_ind))


# special sieve of mu(n) pmin(n) for n <= alpha x^1/3
MU_PMIN = [1] * (ACBRTX + 1)
MU_PMIN[0] = 0
MU = [0] * (ACBRTX + 1)
MU[1] = 1
for j in range(2, ACBRTX + 1):
    if MU_PMIN[j] == 1:
        for i in range(j, ACBRTX + 1, j):
            MU_PMIN[i] = -j if MU_PMIN[i] == 1 else -MU_PMIN[i]

for j in range(2, ACBRTX + 1):
    if MU_PMIN[j] == -j:
        for i in range(j*j, ACBRTX + 1, j * j):
            MU_PMIN[i] = 0

    if MU_PMIN[j] != 0:
        MU[j] = 1 if MU_PMIN[j] > 0 else -1  # integer sgn


def phi_c(y):
    return (y // Q) * PHI_C[Q] + PHI_C[y % Q]


def exact_floor(z, bound_check):
    """
    Exact floor subroutine.

    :param z: initial guess (float within 1 of the true result)
    :param bound_check: exact predicate of z satisfying bound
    :return: largest integer satisfying bound

    https://cs.stackexchange.com/a/4841
    """
    z = int(z) + 1
    while not bound_check(z):
        z -= 1
    return z


def prime_count(x):
    if x < 0:
        raise ValueError

    if x <= Z:
        return PRIME_COUNT_SMALL[x]

    assert ALPHA <= x**(1/6)
    acbrtx = ALPHA * x**(1/3)  # float, may be off
    z = int(x / acbrtx) + 1  # not exact

    # find exact floor of acbrtx
    iacbrtx = exact_floor(acbrtx, lambda z: z**3 <= ALPHA**3 * x)

    a = PRIME_COUNT_SMALL[iacbrtx]  # pi(alpha x^1/3)
    a2 = PRIME_COUNT_SMALL[isqrt(x)]  # pi(x^1/2)
    #print("a a2", a, a2)

    # phi2(x,a)
    P2 = comb(a, 2) - comb(a2, 2)
    for b in range(a+1, a2+1):
        # No recursive call
        P2 += PRIME_COUNT_SMALL[x // PRIMES[b]]

    #print("P2",P2)

    # phi(x,a) Ordinary leaves
    S0 = 0
    for n in range(1, iacbrtx+1):
        # pmin(1) = +inf
        if n == 1 or abs(MU_PMIN[n]) > PRIMES[C]:
            S0 += MU[n] * phi_c(x // n)

    #print("S0",S0)

    # phi(x,a) Special leaves
    S = 0
    # sieve out first C primes
    sieve_ind = [1] * z
    sieve_ind[0] = 0
    for i in range(1, C+1):
        p = PRIMES[i]
        for j in range(p, len(sieve_ind), p):
            sieve_ind[j] = 0

    sieve_c = FenwickTree(sieve_ind)

    for b in range(C, a-1):
        pb1 = PRIMES[b+1]
        if pb1**2 <= iacbrtx:  # Case 1 leaves

            m_min = exact_floor(acbrtx / pb1,
                lambda z: (z * pb1)**3 <= ALPHA**3 * x)

            for m in range(m_min+1, iacbrtx+1):
                if abs(MU_PMIN[m]) > pb1:
                    phi_b = sieve_c.sum_to(x // (m * pb1))
                    S += - MU[m] * phi_b

        else:  # Case 2 leaves
            for d in range(b+2, a+1):
                # trivial leaves
                if max(x // (pb1**2), pb1) < PRIMES[d] <= acbrtx:
                    S += 1
                # easy leaves
                elif (max(x // (pb1**3), pb1) < PRIMES[d]
                      <= min(x // (pb1**2), iacbrtx)):
                    S += PRIME_COUNT_SMALL[x // (pb1 * PRIMES[d])] - b + 1
                else:  # hard leaves
                    S += sieve_c.sum_to(x // (pb1 * PRIMES[d]))

        # sieve out p_(b+1)
        for i in range(pb1, len(sieve_ind), pb1):
            if sieve_ind[i] == 1:
                sieve_c.add_to(i, -1)
                sieve_ind[i] = 0

    #print("S", S)
    return S0 + S + a - P2 - 1


def test_prime_count():
    # A006880
    # 10^12 may cause OOM
    powers_10 = (0, 4, 25, 168, 1229, 9592, 78498, 664579, 5761455, 50847534,
                 455052511, 4118054813, 37607912018)

    for i in range(len(powers_10)):
        assert prime_count(10**i) == powers_10[i]

print(prime_count(X_MAX))


