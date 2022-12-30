"""Commonly used number-theory and helper functions"""
import operator
import random
import itertools
from itertools import accumulate
from functools import reduce
from collections import Counter


########## HELPER FUNCTIONS ##########
def product(iterable):
    """Return the product of the values in the iterable.

    Not to be confused for importing with itertools.product!
    """
    return reduce(operator.mul, iterable, 1)


def powerset(iterable):
    """Return the powerset of the iterable. (from itertools recipes)

    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    from itertools import chain, combinations
    s = list(iterable)
    # can specify min and max size in range for custom powerset
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def memoize(func):
    """Decorates func with an unbounded cache (from functools).

    @functools.cache in Python 3.9+
    """
    from functools import lru_cache
    return lru_cache(maxsize=None)(func)


def timeit(f):
    """Timing decorator for functions.

    Example usage: sieve = timeit(sieve)
    """
    from time import clock
    def timed(*args, **kwargs):
        time_start = clock()
        result = f(*args, **kwargs)
        time_end = clock()

        all_args = list(map(str, args))
        for key in kwargs:
            all_args.append("{}={}".format(key, kwargs[key]))

        print("{}({})   took {:2.4f}s".format(f.__name__, ', '.join(all_args),
                                              time_end - time_start))
        return result

    return timed


########## NUMBER THEORY ##########
def sieve(n):
    """Sieve of Eratosthenes: returns a list of primes strictly below n."""
    nums = [0] * n
    for i in range(2, int(n**0.5)+1):
        if nums[i] == 0:
            for j in range(i*i, n, i):
                nums[j] = 1

    return [i for i in range(2, n) if nums[i] == 0]


def is_prime(n, trials=20):
    """Returns whether a number is prime or not using Miller-Rabin primality.

    First check divisibility by small primes (below 100).
    Deterministic variant by checking small set of potential witnesses.
    Smallest number requiring first n prime numbers is A006945.
    Credit: Albert Sweigart
    """
    PRIME_100 = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53,
                 59, 61, 67, 71, 73, 79, 83, 89, 97}

    assert n >= 0 and isinstance(n, int)  # don't handle negatives
    if n < 2: return False  # 0 and 1 considered not prime

    # Small trial division
    if n in PRIME_100: return True
    if any(n % p == 0 for p in PRIME_100): return False

    s = n - 1
    t = 0
    while s % 2 == 0:
        s = s // 2
        t += 1

    # Testing is_prime set of potential witnesses is big speedup!
    # (n<10^6: 13.8 -> 3.1 s, n<10^7: 136.2 -> 34.9 s)
    # Still twice as slow as gmpy2 though :(
    # Credit: Pomerance, Selfridge, Wagstaff, Jaeschke
    witness_sets = (
        (2047, (2,)),
        (1373653, (2, 3)),
        (25326001, (2, 3, 5)),
        (3215031751, (2, 3, 5, 7)),
        (3474749660383, (2, 3, 5, 7, 11, 13)),
        (341550071728321, (2, 3, 5, 7, 11, 13, 17))
    )

    small_n = False
    for witness_set in witness_sets:
        if n < witness_set[0]:
            witnesses = witness_set[1]
            trials = len(witnesses)
            small_n = True
            break

    for trial in range(trials):
        # WITNESS ME
        if small_n:
            a = witnesses[trial]
        else:
            a = random.randrange(2, n - 1)

        v = pow(a, s, n)
        if v != 1: # this test does not apply if v is 1.
            i = 0
            while v != (n - 1):
                if i == t - 1:
                    return False  # WITNESSED
                else:
                    i = i + 1
                    v = (v ** 2) % n
    return True


def is_square(n):
    """Returns if a number is square without floating point math.

    Uses Babylonian / Heron's method, i.e. Newton's method
    Also consider pre-compute set of squares, or gmpy2.is_square()
    Credit: Alex Martelli
    """
    if n == 1: return True
    x = n // 2
    seen = {x}
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


def factor(n, primes=None):
    """Return all prime factors of n.

    Output dict of (prime, mult) pairs using trial division.
    If `primes` to try is provided, requires list of primes up to sqrt(n)
    Modeled after sympy.ntheory.factorint
    CPython/Pypy 3.6+, dict keys (primes) should be ordered
    """
    assert n > 0  # only have positive integer input

    factors = Counter()
    test_divs = primes if primes else range(2, int(n**0.5)+1)
    for d in test_divs:
        if d * d > n: break
        while n % d == 0:
            n //= d
            factors[d] += 1

    if n > 1: # Only one prime factor >= sqrt(n)
        factors[n] += 1
    return factors


def divisors(prime_powers):
    """Returns divisors given (ordered) factorization dict.

    Ex. `divisors({2:2,3:1})` should return [1,2,3,4,6,12] in some order
    """
    divs = []
    exp_ranges = []
    for p, maxe in prime_powers.items():
        exp_ranges.append([p**e for e in range(maxe+1)])

    for pps in itertools.product(*exp_ranges):
        divs.append(product(pps))

    return divs


def lcm(a, b):
    """Find lcm by reduction of the gcd. math.lcm in Python 3.9+"""
    from math import gcd
    return a * b // gcd(a, b)


def phi(n, primes):
    """Euler's totient function using the product formula.

    Requires primes up to sqrt(n).
    """
    if n == 0: return 0
    r = n
    for p in primes:
        if p*p > n: break
        if n % p == 0:
            while n % p == 0:
                n //= p
            r -= r//p  # r *= (1 - 1/p)

    if n > 1: r -= r // n  # If n had prime factor > sqrt(n)

    return r


def mul_inv(a, m):
    """Modular multiplicative inverse: a^-1 mod m.

    Credit: rosettacode.org
    """
    a = a % m  # handle negative input
    m0 = m
    x0, x1 = 0, 1
    if m == 1: return 1
    while a > 1:
        assert m != 0, "a and m must be coprime"
        q = a // m
        a, m = m, a%m
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += m0
    return x1


# Save calculated values for future use (problem 625)
# "Public" (no leading underscore) for now
totient_sum_large = dict()  # Can implement as array for minor speedup
totient_sum_small = None
totient_small_cutoff = -1

def totient_sum(n):
    """Follows the ideas outlined in my writeup plus sieving for about O(n^2/3)

    Also saves precalculated values in global variables
    https://math.stackexchange.com/a/1740370
    """

    cutoff = int(n**(2/3))
    global totient_small_cutoff

    if cutoff > totient_small_cutoff:
        totient_small_cutoff = cutoff
        # Recalculate small totient range
        totient_range_small = totient_range(cutoff)

        # Convert totient range to totient sum
        global totient_sum_small
        totient_sum_small = list(accumulate(totient_range_small))


    def _Phi(n):
        if n < cutoff:
            return totient_sum_small[n]

        if n in totient_sum_large:
            return totient_sum_large[n]

        isqrtn = int(n**0.5)
        s = n*(n+1)//2
        for x in range(2, isqrtn+1):
            s -= _Phi(n // x)

        for y in range(1, isqrtn + (isqrtn != n // isqrtn)):
            s -= (n//y - n//(y+1)) * _Phi(y)

        totient_sum_large[n] = s
        return s

    return _Phi(n)


mertens_large = dict()
mertens_small = None
mertens_small_cutoff = -1

def mertens(n, primes):
    """Calculates Mertens function M(n).

    Very similar approach to totient sum.
    `primes` must contain primes up to cutoff value n^(2/3)
    https://mathoverflow.net/a/320042
    """
    assert n >= 1
    cutoff = int(n**(2/3))
    global mertens_small_cutoff

    if cutoff > mertens_small_cutoff:
        mertens_small_cutoff = cutoff
        mobius_small = mobius_range(cutoff, primes)
        global mertens_small
        mertens_small = list(accumulate(mobius_small))


    def M(n):
        if n < cutoff:
            global mertens_small
            return mertens_small[n]

        if n in mertens_large:
            return mertens_large[n]

        isqrtn = int(n**0.5)
        s = 1
        for x in range(2, isqrtn+1):
            s -= M(n // x)

        for y in range(1, isqrtn + (isqrtn != n // isqrtn)):
            s -= (n//y - n//(y+1)) * M(y)

        mertens_large[n] = s
        return s

    return M(n)


def totient_range(n):
    """Calculates all totients in a range.

    Using a sieve and Euler's product formula for O(n log log n) time.
    Credit: Marcus Stuhr
    """
    tots = list(range(n+1))
    for p in range(2, n+1):
        if p == tots[p]:
            k = p
            while k <= n:
                tots[k] -= tots[k] // p
                k += p

    return tots


def mobius_range(n, primes):
    """Computes Möbius function for 0 to n using sieve approach.

    Requires `primes` to contain all primes below n.
    https://mathoverflow.net/a/200392
    """
    mus = [1] * (n+1)
    mus[0] = 0
    for p in primes:
        if p > n: break
        for i in range(p, n+1, p):
            mus[i] *= -1
        for i in range(p**2, n+1, p**2):
            mus[i] = 0

    return mus


def ruler(n, p):
    """Calculates max integer a such that p^a divides n."""
    a = 0
    while n % p == 0:
        n //= p
        a += 1
    return a


def int_to_base(n, b):
    """Returns a list of digits in arbitrary base"""
    assert n >= 0  # Untested for negative nums

    if n == 0:
        return [0]
    digits = []
    while n:
        digits.append(int(n % b))
        n //= b
    return digits[::-1]


def pandigital(n, b):
    """Checks if n contains all digits from 0 to b-1"""
    digit_list = int_to_base(n, b)
    return set(digit_list) == set(range(b))


def is_smooth(n, primes):
    """Test if n has only factors in primes"""
    for p in primes:
        while n % p == 0:
            n //= p

    return n == 1


def prime_count_sieve(n, primes):
    """Poor man's prime-counting function.

    Requires a sorted list of primes with primes[0] == 2
    """
    assert primes[0] == 2
    from bisect import bisect
    return bisect(primes, n)


# Global list because python, though supposedly passing by assignment, runs way
# faster with the globals :/
# I have yet to figure out passing efficiently (and the whole exercise is
# largely pointless compared to rewriting in a faster language)
_prime_count_p = None
_prime_count_limit = 10**4

@memoize
def _phi(x, a):
    if a == 1:
        return (x + 1) // 2
    return _phi(x, a-1) - _phi(x // _prime_count_p[a], a-1)


@memoize
def _pi(n):
    if n < _prime_count_limit:
        return prime_count_sieve(n, _prime_count_p[1:])

    z = int((n + 0.5)**0.5)
    a = _pi(int(z**0.5 + 0.5))
    b = _pi(z)
    c = _pi(int(n**(1/3) + 0.5))
    s = _phi(n, a) + (b+a-2)*(b-a+1)//2

    for i in range(a+1, b+1):
        w = n / _prime_count_p[i]
        lim = _pi(int(w**0.5))
        s -= _pi(int(w))
        if i <= c:
            for j in range(i, lim+1):
                s += -_pi(int(w / _prime_count_p[j])) + j - 1
    return s


def prime_count(n):
    """Prime-counting function using the Meissel-Lehmer algorithm.

    Algorithm credit: user448810 (programming praxis)
    Fiddly rounding from danaj (Dana Jacobsen)
    https://programmingpraxis.com/
    2011/07/22/counting-primes-using-legendres-formula/#comment-5958
    """
    # a-th prime for small a (1-indexed)
    global _prime_count_p
    sieve_max = int(n**0.5)+1  # can be optimized

    # Recreate sieve if current sieve is smaller than new sieve
    if _prime_count_p == None or _prime_count_p[-1] < sieve_max:
        _prime_count_p = [None] + sieve(max(_prime_count_limit, sieve_max))

    return _pi(n)


def fib_list(n):
    """Returns list of Fibonacci nums up to F_n, with F[0] = 0 and F[1] = 1"""
    fib = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib


def combination(n, k):
    return product(range(n-k+1, n+1)) // product(range(1, k+1))


def permutation(n, k):
    return product(range(n-k+1, n+1))


if __name__ == "__main__":
    pass
