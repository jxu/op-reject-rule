"""Unit tests to ensure commonly used number functions are correct."""

import pytest
from bisect import bisect
from number import *
from itertools import accumulate

def test_is_prime_small():
    with pytest.raises(Exception):
        is_prime(-1)

    assert not is_prime(0)
    assert not is_prime(1)

    primes_1000 = sieve(1000)

    for n in range(2, 1000):
        assert is_prime(n) == (n in primes_1000)



def test_is_prime_spsp():
    """Tests smallest n strong pseudoprime to first k primes: A014233"""
    strong_pseudoprimes = (
        2047, 1373653, 25326001, 3215031751, 2152302898747, 3474749660383,
        341550071728321, 3825123056546413051)
    for sp in strong_pseudoprimes:
        assert not is_prime(sp), sp


def test_phi():
    """Checks Euler's totient function against known values"""
    phi_values = (0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4)  # A000010
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
    # A000010
    assert totient_range(10) == [0, 1, 1, 2, 2, 4, 2, 6, 4, 6, 4]


def test_totient_sum():
    tot_range = totient_range(10**5)
    totsum_range = list(accumulate(tot_range))

    # A064018
    assert totient_sum(100, totsum_range) == 3044
    assert totient_sum(10**8, totsum_range) == 3039635516365908
    #assert totient_sum(10**11) == 3039635509283386211140

def test_is_square():
    assert is_square(1)
    assert not is_square(2)
    assert not is_square(120)
    assert is_square(121)
    assert is_square(12345678987654321234567 ** 2)
    assert not is_square(12345678987654321234567 ** 2 - 1)


def test_pollard_rho():
    for n in range(10, 1000):
        if is_prime(n): continue
        d = pollard_rho(n)
        # non-trivial divisor
        assert d != 1 and d != n and n % d == 0


def test_factor():
    facts = {
        1: {}, 
        2: {2:1}, 
        3: {3:1}, 
        4: {2:2}, 
        5: {5:1}, 
        6: {2:1,3:1}, 
        7: {7:1},
        8: {2:3}, 
        9: {3:2}, 
        10: {2:1,5:1}, 
        11: {11:1}, 
        12: {2:2,3:1}, 
        13: {13:1}, 
        14: {2:1,7:1}, 
        15: {3:1,5:1},
        25: {5:2},
        60: {2:2,3:1,5:1},
        61: {61:1},
        103*107: {103:1,107:1},
        1009: {1009:1},
        1009**2: {1009:2},
        10007: {10007:1},
        10007*10009: {10007:1,10009:1},
        (10**9+7)*(10**9+9): {10**9+7:1,10**9+9:1},
    }

    with pytest.raises(ValueError):
        factor(0)

    for n in facts:
        assert factor(n) == facts[n]


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


def test_int_to_base():
    assert int_to_base(16, 16) == [1, 0]


def test_fib_list():
    assert fib_list(5) == [0, 1, 1, 2, 3, 5]


def test_linear_sieve():
    # A020639 (except a(1) = 1)
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


def test_mobius_range():
    # A008683
    small_mus = [1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1,0,-1,0,-1,
                 0,1,1,-1,0,0,1,0,0,-1,-1]

    assert mobius_range(len(small_mus))[1:] == small_mus
