"""Commonly used number-theory and helper functions"""
import operator
import math
import random
import itertools
from math import prod, gcd
from itertools import accumulate
from functools import reduce, cache, wraps
from collections import Counter



########## HELPER FUNCTIONS ##########

def powerset(iterable):
    """Return the powerset of the iterable. (from itertools recipes)

    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    from itertools import chain, combinations
    s = list(iterable)
    # can specify min and max size in range for custom powerset
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def timeit(f):
    """Timing decorator for functions.

    Example usage: sieve = timeit(sieve)
    """
    from time import time
    def timed(*args, **kwargs):
        time_start = time()
        result = f(*args, **kwargs)
        time_end = time()

        all_args = list(map(str, args))
        for key in kwargs:
            all_args.append("{}={}".format(key, kwargs[key]))

        print("{}({})\ttook {:2.2f}s".format(f.__name__, ', '.join(all_args),
                                             time_end - time_start))
        return result

    return timed


def memoize_first(func):
    """Memoize like functools.cache, but only consider first argument.

    Adapted from https://wiki.python.org/moin/PythonDecoratorLibrary
    """
    cache = func.cache = {}

    @wraps(func)
    def memoizer(arg1, *args):
        if arg1 not in cache:
            cache[arg1] = func(arg1, *args)
        return cache[arg1]
    return memoizer

########## NUMBER THEORY ##########

def extended_euclidean(a, b):
    """Returns g, x, y for which a*x + b*y = g = gcd(a,b).

    Credit: e-maxx.ru (Ivanov Maxim)
    """
    if b == 0:
        return a, 1, 0
    d, x1, y1 = extended_euclidean(b, a % b)
    x, y = y1, x1 - y1 * (a // b)
    return d, x, y


def crt(rs, mods):
    """Chinese Remainder Theorem for x = r[i] mod m[i]

    Returns solution (r, m) of x = r mod m, with m = m1*m2*...
    Exact solution from Wikipedia
    """
    assert len(rs) == len(mods)
    r0, m0 = rs[0], mods[0]

    for i in range(1, len(mods)):
        r1, m1 = rs[i], mods[i]
        g, n0, n1 = extended_euclidean(m0, m1)
        r0 = (r0*n1*m1 + r1*n0*m0) % (m0*m1)
        m0 *= m1

    return r0 % m0, m0


def sieve(n):
    """Sieve of Eratosthenes: returns a list of primes <= n.

    Only sieves by odd numbers to fit more into cache.
    """
    if n < 2: return []
    comp = bytearray((n+1)//2)
    for i in range(3, int((n+1)**0.5)+1, 2):
        if comp[i//2] == 0:
            for j in range(i*i, n+1, 2*i):
                comp[j//2] = 1

    return [2] + [i for i in range(3, n+1, 2) if comp[i//2] == 0]


def linear_sieve(n):
    """Compute least primes array up to n using the linear sieve.
    lp[i] = least prime factor of i

    Credit: Paul Pritchard
    """
    lp = [0] * (n+1)
    pr = []
    for i in range(2, n+1):
        if lp[i] == 0:
            lp[i] = i
            pr.append(i)

        for j in range(len(pr)):
            x = i * pr[j]
            if x > n: break
            lp[x] = pr[j]
            if pr[j] == lp[i]: break

    return lp


def linear_sieve_factors(lp, n):
    """Factorizes n given least primes array from linear_sieve.

    Factorization given in prime powers form like factorize
    """
    pp = Counter()
    while n > 1:
        pp[lp[n]] += 1
        n //= lp[n]
    return pp


def is_prime(n):
    """Miller test if n is composite or (probably) prime
    
    First check divisibility by small primes (below 100).
    Deterministic up to 2^64 by checking small set of potential witnesses.
    Note: For repeated small n, checking in a prime set might be better.
    """
    if not isinstance(n, int):  # don't accept floats
        raise TypeError  
    if n < 0:  # don't accept negatives 
        raise ValueError
    if n < 2: 
        return False  # 0 and 1 considered not prime

    PRIME_12 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37)

    # Small trial division
    if n in PRIME_12: 
        return True

    for p in PRIME_12:
        if n % p == 0: 
            return False

    if n < 4759123141:
        witness_set = (2, 3, 5, 7, 61)
    else: 
        # A014233(12) guaranteed up to 318665857834031151167461 > 2^64
        witness_set = PRIME_12 
            
    u = n - 1   
    t = 0
    while u % 2 == 0:
        u, t = u // 2, t + 1

    for a in witness_set:
        if a > n - 2: continue
        
        x = pow(a, u, n)
        for i in range(t):
            y = x**2 % n  # x = x_i, y = x_{i-1}
            if y == 1 and x != 1 and x != n-1:
                return False
            x = y 
        if y != 1:
            return False
        
    return True


def is_square(n):
    """Returns if a number is square without floating point math.

    Also consider pre-compute set of squares
    """
    return n == math.isqrt(n)**2


def factor(n, primes):
    """Return prime factorization of n as dict of prime:exponent pairs.

    Output dict of prime:exponent pairs using trial division.
    Modeled after sympy.ntheory.factorint
    CPython/Pypy 3.6+, dict keys (primes) should be ordered
    """
    if n <= 0:
        raise ValueError

    factors = Counter()

    #if is_prime(n):
    #    return Counter({n:1})
    
    for d in primes:
        if d * d > n: break
        while n % d == 0:
            n //= d
            factors[d] += 1



    if n > 1: # Only one prime factor >= sqrt(n)
        factors[n] += 1
    return factors


def divisors(prime_powers, proper=False):
    """Returns divisors given (ordered) factorization dict.

    Ex. `divisors({2:2,3:1})` should return [1,2,3,4,6,12] in some order
    """
    divs = []
    exp_ranges = []
    n = 1
    for p, maxe in prime_powers.items():
        exp_ranges.append([p**e for e in range(maxe+1)])
        n *= p**maxe

    for pps in itertools.product(*exp_ranges):
        if not proper or prod(pps) != n:
            divs.append(prod(pps))

    return divs


def phi(n, factors=None):
    """Euler's totient function, using the product formula.

    :param n: n
    :param factors: if provided, should be prime powers dict
    :return: phi(n)
    """
    if n == 0: return 0
    if factors is None:
        factors = factor(n)
    r = n
    for p, e in factors.items():
        r -= r//p
    return r


def mul_order(a, n, phi_n=None, factors_phi=None):
    """Compute the multiplicative order of a mod n.

    Algorithm from Bach & Shallit, Algorithmic Number Theory
    https://rosettacode.org/wiki/Multiplicative_order
    For phi(n) = q1^e1 ... qk^ek, let yi = phi(n) without qi factors,
    xi = a^yi mod n, then raise to qi power mod n until xi = 1, then the min
    necessary qi's have been factored into order.

    See 417.py for more tricks with CRT.

    :param a: element of (Z/nZ)*, coprime to n
    :param n: modulus
    :param phi_n: the order of group (Z/nZ)*, if available
    :param factors_phi: factorization of phi(n), if available
    :return: ord_n(a)
    """
    if gcd(a, n) != 1:
        raise ValueError

    if phi_n is None:
        phi_n = phi(n)
    if factors_phi is None:
        factors_phi = factor(phi_n)

    order = 1
    for qi, ei in factors_phi.items():
        yi = phi_n // (qi ** ei)
        xi = pow(a, yi, n)
        while xi != 1:
            xi = pow(xi, qi, n)
            order *= qi

    return order


def mod_inv(a, m):
    """Modular multiplicative inverse: a^-1 mod m.

    Based on extended Euclidean algorithm
    """
    g, x, y = extended_euclidean(a, m)
    if g != 1:
        raise ValueError("No modular inverse")
    return x % m


def mod_inv_range(p, end=None):
    """Computes inverse mod p in range [1, end] in O(end) time

    Credit: cp-algorithms, e-maxx.ru
    """
    if end is None: end = p-1
    inv = [None] * (end+1)
    inv[1] = 1
    for i in range(2, end+1):
        inv[i] = (-(p//i) * inv[p%i]) % p
    return inv


def mobius_range(n):
    """Computes Möbius function for [0, n] using a modified sieve approach.

    Rick Sladkey has a fancier version that avoids going through prime again
    in exchange for storing the entire i https://mathoverflow.net/a/99545
    TODO: profile 
    """
    primes = sieve(n)    
    mus = [1] * (n+1)
    
    for p in primes:
        for i in range(p, n+1, p):
            mus[i] *= -1
        for i in range(p**2, n+1, p**2):
            mus[i] *= 0

    return mus


def totient_range(n):
    """Calculates all totients in a range.

    Using a sieve and Euler's product formula for O(n log log n) time.
    Credit: Marcus Stuhr
    """
    tots = list(range(n+1))
    for p in range(2, n+1):
        if p == tots[p]:
            for k in range(p, n+1, p):
                tots[k] -= tots[k] // p

    return tots


def totient_sum_range(tot_range):
    """Helper function for pre-computing values for totient_sum"""
    return list(accumulate(tot_range))


@memoize_first
def totient_sum(n, totsum_range):
    """Calculates the totient sum up to n in sub-linear time.

    totsum_range is a list of precomputed totient sums, should be up to 
    about n^2/3 for performance.
    
    Totient sum calculation: Dirichlet hyperbola like methods I explain at
    https://math.stackexchange.com/a/1740370
    
    Basically starting with T(n) = Sum_{i=1..n} Phi(n//i), rearrange
    Phi(n) = T(n) Sum_{i=2..n} Phi(n//i)
    The observation is n//i is constant for large i, so count precisely how 
    many times each j = n//i value occurs.
    """
    
    if n < len(totsum_range):
        return totsum_range[n]

    c = int(n**0.5)  # can adjust but sqrt n seems to work the best
    s = n * (n + 1) // 2

    for m in range(2, n//c + 1):
        s -= totient_sum(n // m, totsum_range)

    for k in range(1, c):
        s -= (n//k - n//(k+1)) * totient_sum(k, totsum_range)

    return s
    

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


def fib_list(n):
    """Returns list of Fibonacci numbers up to F_n (with F_0 = 0)"""
    assert n >= 1
    fib = [0, 1] + [0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i-2]
    return fib

def fact_mod_list(n, m):
    """Compute [0!, ..., n!] mod m in O(n)."""
    fact_mod = [1] * (n + 1)
    for i in range(2, n+1):
        fact_mod[i] = (i * fact_mod[i-1]) % m
    return fact_mod


def inv_list(l, m):
    """Inverse mod m of every value in l."""
    return [mod_inv(x,m) for x in l]

### ALGORITHM
def binary_search(f, l, r):
    """Return L s.t. f(L)=0, f(L+1)=f(R)=1, if it exists

    TODO: document more
    """
    while r - l > 1:
        m = (l + r) // 2
        if f(m): r = m
        else: l = m

    return l


if __name__ == "__main__":
    pass
