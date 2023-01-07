"""Unit tests to ensure commonly used number functions are valid."""
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
    small_primes = (2, 3)
    primes = sieve(10)
    phi_values = (1, 1, 2, 2, 4, 2, 6, 4, 6, 4)
    for n in range(10):
        assert phi(n+1, small_primes) == phi_values[n]

    assert phi(100, primes) == 40


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
    assert sieve(5) == [2, 3]
    assert sieve(100) == primes_100
    assert len(sieve(10000)) == 1229


def test_powerset():
    assert tuple(powerset([1,2,3])) == \
           ((), (1,), (2,), (3,), (1, 2), (1, 3), (2, 3), (1, 2, 3))


def test_mul_inv():
    with pytest.raises(Exception):
        mul_inv(7, 7)

    for a in range(1, 7):
        assert mul_inv(a, 7) == (None, 1, 4, 5, 2, 3, 6)[a]

    assert mul_inv(-1, 7) == -1 % 7


def test_ruler():
    for n in range(1, 11):
        assert ruler(n, 2) == [None,0,1,0,2,0,1,0,3,0,1][n]


def test_int_to_base():
    assert int_to_base(16, 16) == [1, 0]