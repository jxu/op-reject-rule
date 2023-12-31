# Consecutive pairs of p-smooth numbers are given by Størmer's theorem
# Procedure given by Lehmer. Number of pairs is A002071

# Solving x^2 - 2qy^2 = 1, where q is square-free and 47-smooth
# From Lehmer's paper Table A, there are 869 pairs for 41-smooth numbers.
# So I estimate < 1500 pairs for 47-smooth
# Theorem 7 gives bounds for largest smooth pair, but they are extremely weak
# ex. S_1(13) < 10^10^9.925 ??
# According to M. F. Hasler at A002072, for n primes, 10^n/n is an upper bound
# except for n=4.

# Attempt simple recursive solution with guess at max smooth number.
# Curiously, using Størmer's Theorem and solving 2^15 - 1 Pell's equations with
# SymPy is significantly slower than the easy recursive generation solution.
# This is because I don't have any way of stopping SymPy from finding
# ridiculously large (70+ digits) fundamental solutions of Pell's equations.

# 10s with PyPy, 55s with python 3.5
from number import sieve

def is_smooth(n, primes):
    """Test if n has only factors in primes"""
    assert n >= 2
    for p in primes:
        while n % p == 0:
            n //= p

    return n == 1


def test_is_smooth():
    small_primes = [2, 3]
    for n in range(2, 11):
        assert is_smooth(n, small_primes) == \
               (None, None, True, True, True, False,
                True, False, True, True, False)[n]


MAX_SMOOTH = 10**13  # Same for 10**14 and 10**15
p = 47

primes = sieve(p+1)
pairs = 0
indices_sum = 0

def f(n, min_prime_index):
    if n > MAX_SMOOTH or min_prime_index >= len(primes):
        return

    if is_smooth(n+1, primes):
        print(n, n+1)
        global indices_sum, pairs
        pairs += 1
        indices_sum += n

    for i in range(min_prime_index, len(primes)):
        f(n * primes[i], i)

f(1, 0)

print("Pairs:", pairs)
print("Indices sum:", indices_sum)
