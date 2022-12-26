"""Unit tests to ensure commonly used number functions are valid."""
import pytest
import number

def test_is_prime_edge_cases():
    assert not number.is_prime(-2)
    assert not number.is_prime(-1)
    assert not number.is_prime(0)
    assert not number.is_prime(1)


def test_is_prime_100():
    primes_100 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47,
                  53, 59, 61, 67, 71, 73, 79, 83, 89, 97}

    for n in range(2, 100):
        assert number.is_prime(n) == (n in primes_100)


def test_is_prime_strong_pseudoprimes():
    """Tests strong pseudoprimes base 2: A001262"""
    strong_pseudoprimes = (2047, 3277, 4033, 4681, 8321, 15841, 29341,
                           42799, 49141, 52633, 65281, 74665, 80581, 85489,
                           88357, 90751, 104653, 130561, 196093, 220729)
    for sp in strong_pseudoprimes:
        assert not number.is_prime(sp), sp


def test_is_prime_deterministic_nums():
    """Tests special odd numbers that fail deterministic tests of first n
    primes: A014233
    """
    terms = (2047, 1373653, 25326001, 3215031751, 2152302898747,
             3474749660383, 341550071728321,
             3825123056546413051, 318665857834031151167461,
             3317044064679887385961981)
    for n in terms:
        assert not number.is_prime(n), n


def test_phi():
    """Checks Euler's totient function against known values"""
    primes = number.sieve(10)
    phi_values = (1, 1, 2, 2, 4, 2, 6, 4, 6, 4)
    for n in range(10):
        assert number.phi(n+1, primes) == phi_values[n], n

    assert number.phi(100, primes) == 40


def test_totient_sum():
    powers_10 = [1, 32, 3044, 304192, 30397486, 3039650754, 303963552392,
                 30396356427242]
    for i in range(len(powers_10)):
        assert number.totient_sum(10**i) == powers_10[i]


def test_is_square():
    assert number.is_square(1)
    assert not number.is_square(2)
    assert not number.is_square(120)
    assert number.is_square(121)
    assert number.is_square(12345678987654321234567 ** 2)


def test_prime_count():
    small_values = (0,0,1,2,2,3,3,4,4,4,4,5,5,6,6,6,6,7,7,8,8)
    for i in range(len(small_values)):
        assert number.prime_count(i) == small_values[i]

    powers_10 = (0, 4, 25, 168, 1229, 9592, 78498, 664579)

    for i in range(len(powers_10)):
        assert number.prime_count(10**i) == powers_10[i]


def test_mobius_range():
    small_mus = [0,1,-1,-1,0,-1,1,-1,0,0,1,-1,0,-1,1,1,0,-1,0,-1,
                 0,1,1,-1,0,0,1,0,0,-1,-1]
    n = len(small_mus)-1
    primes = number.sieve(n)

    assert number.mobius_range(n, primes) == small_mus


def test_mertens_small():
    primes = number.sieve(10)
    mertens_small = (0,1,0,-1,-1,-2,-1,-2,-2,-2,-1,-2,
                     -2,-3,-2,-1,-1,-2,-2,-3,-3)
    for i in range(1, len(mertens_small)):
        assert number.mertens(i, primes) == mertens_small[i]


def test_mertens_pow10():
    primes = number.sieve(10**5)
    powers_10 = (1, -1, 1, 2, -23, -48, 212, 1037)
    for i in range(1, len(powers_10)):
        assert number.mertens(10**i, primes) == powers_10[i]


def test_factor():
    from number import factor
    primes = [2, 3, 5]
    factorizations = (None, {}, {2:1}, {3:1}, {2:2}, {5:1}, {2:1,3:1}, {7:1},
                      {2:3}, {3:2},{2:1,5:1})

    with pytest.raises(Exception):
        factor(0, primes)

    for n in range(1, len(factorizations)):
        assert factor(n, primes) == factorizations[n]

    assert factor(17, primes) == {17: 1}
    assert factor(25, primes) == {5: 2}

    with pytest.raises(Exception):
        factor(30, primes)
