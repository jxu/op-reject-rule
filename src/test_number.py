"""Unit tests to ensure commonly used number functions are correct."""
import pytest
from number import *

def test_is_prime_small():
    with pytest.raises(Exception):
        is_prime(-1)

    assert not is_prime(0)
    assert not is_prime(1)

    primes_100 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

    for n in range(2, 100):
        assert is_prime(n) == (n in primes_100)


def test_is_prime_strong_pseudoprimes():
    """Tests strong pseudoprimes base 2: A001262"""
    strong_pseudoprimes = (2047, 3277, 4033, 4681, 8321, 15841, 29341,
                           42799, 49141, 52633, 65281, 74665, 80581, 85489,
                           88357, 90751, 104653, 130561, 196093, 220729)
    for sp in strong_pseudoprimes:
        assert not is_prime(sp), sp


def test_is_prime_deterministic_nums():
    """Tests special odd numbers that fail deterministic tests of first n
    primes: A014233
    """
    terms = (2047, 1373653, 25326001, 3215031751, 2152302898747,
             3474749660383, 341550071728321,
             3825123056546413051, 318665857834031151167461,
             3317044064679887385961981)
    for n in terms:
        assert not is_prime(n), n


def test_phi():
    """Checks Euler's totient function against known values"""
    phi_values = (0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4)
    for n in range(1, len(phi_values)):
        assert phi(n) == phi_values[n]

    assert phi(100) == 40


def test_mul_order():
    mod5_cases = ((1,1), (2,4), (3,4), (4,2))
    mod10_cases = ((1,1), (3,4), (7,4), (9,2))
    for a, o in mod5_cases:
        assert mul_order(a, 5) == o
    for a, o in mod10_cases:
        assert mul_order(a, 10) == o

    with pytest.raises(ValueError): mul_order(2, 10)
    assert mul_order(3, 61) == 10


def test_totient_range():
    assert totient_range(10) == [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4]


def test_totient_sum():
    powers_10 = [1, 32, 3044, 304192, 30397486, 3039650754, 303963552392,
                 30396356427242]
    for i in range(len(powers_10)):
        assert totient_sum(10**i) == powers_10[i]


def test_is_square():
    assert is_square(1)
    assert not is_square(2)
    assert not is_square(120)
    assert is_square(121)
    assert is_square(12345678987654321234567 ** 2)
    assert not is_square(12345678987654321234567 ** 2 - 1)


def test_isqrt():
    isqrts = (0,1,1,1,2,2,2,2,2,3,3,3,3,3,3,3,4,4)

    for i in range(len(isqrts)):
        assert isqrt(i) == isqrts[i]


def test_prime_count():
    small_values = (0,0,1,2,2,3,3,4,4,4,4,5,5,6,6,6,6,7,7,8,8)
    for i in range(len(small_values)):
        assert prime_count(i) == small_values[i]

    powers_10 = (0, 4, 25, 168, 1229, 9592, 78498, 664579)

    for i in range(len(powers_10)):
        assert prime_count(10**i) == powers_10[i]


def test_mobius_range():
    small_mus = [0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1,0,-1,0,-1,
                 0,1,1,-1,0,0,1,0,0,-1,-1]
    n = len(small_mus)-1
    primes = sieve(n)

    assert mobius_range(n, primes) == small_mus


def test_mertens_small():
    primes = sieve(10)
    mertens_small_ = (0,1,0,-1,-1,-2,-1,-2,-2,-2,-1,-2,
                      -2,-3,-2,-1,-1,-2,-2,-3,-3)
    for i in range(1, len(mertens_small_)):
        assert mertens(i, primes) == mertens_small_[i]


def test_mertens_pow10():
    primes = sieve(10**5)
    powers_10 = (1, -1, 1, 2, -23, -48, 212, 1037)
    for i in range(1, len(powers_10)):
        assert mertens(10**i, primes) == powers_10[i]


def test_factor():
    small_primes = [2, 3, 5]
    factorizations = (None, {}, {2:1}, {3:1}, {2:2}, {5:1}, {2:1,3:1}, {7:1},
                      {2:3}, {3:2}, {2:1,5:1}, {11:1}, {2:2,3:1}, {13:1},
                      {2:1,7:1})

    with pytest.raises(Exception):
        factor(0, small_primes)

    for n in range(1, len(factorizations)):
        assert factor(n, small_primes) == factorizations[n]
        assert factor(n) == factorizations[n]

    assert factor(17, small_primes) == {17: 1}
    assert factor(25, small_primes) == {5: 2}
    assert factor(60, small_primes) == {2:2, 3:1, 5:1}
    assert factor(61, small_primes) == {61: 1}


def test_divisors():
    assert sorted(divisors({})) == [1]
    assert sorted(divisors({2:1})) == [1, 2]
    assert sorted(divisors({2:2})) == [1, 2, 4]
    assert sorted(divisors({2:1, 3:1})) == [1, 2, 3, 6]
    assert sorted(divisors({2:2, 3:1})) == [1, 2, 3, 4, 6, 12]


def test_sieve():
    primes_100 = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
    assert sieve(3) == [2, 3]
    assert sieve(4) == [2, 3]
    assert sieve(5) == [2, 3, 5]
    assert sieve(7) == [2, 3, 5, 7]
    assert sieve(9) == [2, 3, 5, 7]
    assert sieve(100) == primes_100
    assert len(sieve(10000)) == 1229
    assert len(sieve(9973)) == 1229


def test_powerset():
    assert tuple(powerset([1,2,3])) == \
           ((), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3))


def test_mod_inv():
    with pytest.raises(Exception):
        mod_inv(7, 7)

    for a in range(1, 7):
        assert mod_inv(a, 7) == (None, 1, 4, 5, 2, 3, 6)[a]

    assert mod_inv(-1, 7) == 6


def test_ruler():
    for n in range(1, 11):
        assert ruler(n, 2) == [None,0,1,0,2,0,1,0,3,0,1][n]


def test_int_to_base():
    assert int_to_base(16, 16) == [1, 0]


def test_is_smooth():
    small_primes = [2, 3]
    for n in range(2, 11):
        assert is_smooth(n, small_primes) == \
               (None, None, True, True, True, False,
                True, False, True, True, False)[n]


def test_fib_list():
    assert fib_list(5) == [0, 1, 1, 2, 3, 5]


def test_comb():
    for i in range(5):
        assert comb(4, i) == (1, 4, 6, 4, 1)[i]


def test_perm():
    for i in range(5):
        assert perm(4, i) == (1, 4, 12, 24, 24)[i]


def test_linear_sieve():
    assert linear_sieve(11) == [0, 0, 2, 3, 2, 5, 2, 7, 2, 3, 2, 11]


def test_factors_from_linear_sieve():
    lp = linear_sieve(10)
    for n in range(1, 11):
        assert linear_sieve_factors(lp, n) == factor(n)


def test_extended_euclidean():
    assert extended_euclidean(0, 1) == (1, 0, 1)
    assert extended_euclidean(85, 15) == (5, -1, 6)


def test_crt():
    assert crt((2, 3), (3, 5)) == (8, 15)
    assert crt((2, 3, 2), (3, 5, 7)) == (23, 105)


def test_mod_inv_range():
    assert mod_inv_range(5) == [None, 1, 3, 2, 4]
