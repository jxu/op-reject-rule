"""Commonly used number-theory and helper functions"""
import operator
import random
import itertools
from collections import Counter

PRIME_100 = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59,
             61, 67, 71, 73, 79, 83, 89, 97)
PRIME_100_SET = set(PRIME_100)

########## HELPER FUNCTIONS ##########
def take_closest(l, n):
    """Returns closest value to n in sorted list l, via binary search.

    If two numbers are equally close, return the smallest number.
    Credit: Lauritz V. Thaulow
    """
    from bisect import bisect_left
    pos = bisect_left(l, n)
    if pos == 0:
        return l[0]
    if pos == len(l):
        return l[-1]
    before = l[pos - 1]
    after = l[pos]
    if after - n < n - before:
       return after
    else:
       return before


def product(iterable):
    product = 1
    for i in iterable: product *= i  # No reduce() :(
    return product


def accumulate(iterable, func=operator.add):
    """Return running totals, like itertools.accumulate"""
    it = iter(iterable)
    try:
        total = next(it)
    except StopIteration:
        return
    yield total
    for element in it:
        total = func(total, element)
        yield total


def powerset(iterable):
    """From itertools recipes
    powerset([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)
    """
    from itertools import chain, combinations
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s) + 1))


def custom_powerset(s, min_size, max_size):
    from itertools import chain, combinations
    return chain.from_iterable(
        combinations(s, r) for r in range(min_size, max_size+1))


def memoize(obj):
    """Decorator that memoizes a function's calls. Credit: Python wiki"""
    # ignores **kwargs
    from functools import wraps
    cache = obj.cache = {}

    @wraps(obj)
    def memoizer(*args, **kwargs):
        if args not in cache:
            cache[args] = obj(*args, **kwargs)
        return cache[args]

    return memoizer


def timeit(f):
    """Timing decorator for functions. Example usage: sieve = timeit(sieve)"""
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


def unique_permutations(elements):
    """Like itertools.permutations but without duplicates. Credit: Luka Rahne"""

    class unique_element:
        def __init__(self, value, occurrences):
            self.value = value
            self.occurrences = occurrences

    eset=set(elements)
    listunique = [unique_element(i,elements.count(i)) for i in eset]
    u=len(elements)
    return perm_unique_helper(listunique,[0]*u,u-1)


def perm_unique_helper(listunique,result_list,d):
    if d < 0:
        yield tuple(result_list)
    else:
        for i in listunique:
            if i.occurrences > 0:
                result_list[d]=i.value
                i.occurrences-=1
                for g in  perm_unique_helper(listunique,result_list,d-1):
                    yield g
                i.occurrences+=1


def combo_max_product(X, terms, max_product):
    '''Like itertools.combinations(X, terms) but only picks values whose
    product is <= max_product.
    '''
    assert sorted(X) == X  # To keep track of index
    result = []

    def f(last_i, terms_so_far, product_):
        if len(terms_so_far) == terms:
            result.append(terms_so_far)
            return

        for i in range(last_i, len(X)):
            new_product = product_ * X[i]
            if new_product <= max_product:
                f(i+1, terms_so_far + [X[i]], new_product)
            else:  # Product too large already
                break

    f(0, [], 1)
    return result

########## NUMBER THEORY ##########
def sieve(n):
    """Sieve of Eratosthenes: returns a list of primes below n.

    About O(n)
    """
    nums = [0] * n
    for i in range(2, int(n**0.5)+1):
        if nums[i] == 0:
            for j in range(i*i, n, i):
                nums[j] = 1

    return [i for i in range(2, n) if nums[i] == 0]


def is_prime(n, trials=20):
    """Returns whether a number is prime or not using Miller-Rabin.

    First check divisibility by small primes (below 100).
    Deterministic variant by checking small set of potential witnesses.
    Smallest number requiring first n prime numbers is A006945.
    Credit: Albert Sweigart
    """
    if n < 2: return False
    # Small trial division
    if n in PRIME_100_SET: return True
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

    Also consider gmpy2.is_square()
    Credit: Alex Martelli
    """
    if n == 1: return True
    x = n // 2
    seen = set([x])
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in seen: return False
        seen.add(x)
    return True


def is_square_fp(n):
    """Returns if a number is square, avoiding _some_ floating point errors."""
    return int(n**0.5 + 0.5)**2 == n


def factor(n, primes):
    """Return all prime factors of n.

    Output dict of (prime, mult) pairs, requiring list of primes up to sqrt(n)
    Modeled after sympy.ntheory.factorint, but uses trial division
    CPython/Pypy 3.6+, dict keys (primes) should be ordered
    """
    assert n > 0  # only have positive integer input

    factors = Counter()
    for p in primes:
        if p * p > n: break
        while n % p == 0:
            n //= p
            factors[p] += 1

    if n > 1: # Only one prime factor >= sqrt(n)
        factors[n] += 1
    return factors


def divisors(prime_powers):
    """Returns sorted divisors given (ordered) factorization dict."""
    divs = []
    exponent_ranges = (range(e+1) for e in prime_powers.values())
    ps = tuple(prime_powers.keys())
    for es in itertools.product(*exponent_ranges):
        d = 1
        for i in range(len(es)):
            d *= ps[i] ** es[i]
        divs.append(d)
    return divs


def gcd(a, b):
    """Identical to fractions.gcd(a, b) (Euclid's algorithm)"""
    while b:
        a, b = b, a%b
    return a


def lcm(a, b):
    """Find lcm by reduction of the gcd"""
    return a * b // gcd(a, b)


def lcm_n(n):
    """Find lcm of integers 1 to n.

    Skip calculating for 1 to n/2 since those are covered by the upper half
    """
    x = 1
    for i in range(max(n//2, 1), n+1):
        x = lcm(x, i)
    return x


def phi(n, primes):
    """Euler's totient function, using his product formula."""
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


def totient_sum_79(N):
    """Find the sum of phi(n) for 1 to N.

    O(log n) space, O(n^(3/4)) time
    Modified from PE 73 overview. Credit: daniel.is.fischer
    See benchmarks file
    """

    if N < 3:
        return (0, 1, 2)[N]

    K = int((N/2)**0.5)
    M = N // (2*K+1)
    rsmall = [0]*(M+1)
    rlarge = [0]*K

    def F(n):
        return n*(n-1)//2

    def R(n):
        switch = int((n/2)**0.5)
        count = F(n) - F(n//2)
        m = 1
        k = n//2
        while k >= switch:
            nextk = (n // (m+1) - 1) // 2
            count -= (k - nextk)*rsmall[m]
            k = nextk
            m += 1

        while k > 0:
            m = n // (2*k+1)
            if m <= M:
                count -= rsmall[m]
            else:
                count -= rlarge[((N//m) - 1) // 2]
            k -= 1

        if n <= M:
            rsmall[n] = count
        else:
            rlarge[((N//n) - 1) // 2] = count


    for n in range(1, M+1):
        R(n)

    for j in range(K-1, -1, -1):
        R(N // (2*j + 1))

    return rlarge[0] + 1


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


def is_close(a, b, tol=1e-9):
    return abs(a-b) <= tol


def is_int(n):
    return is_close(n, round(n))


def combination(n, k):
    return product(range(n-k+1, n+1)) // product(range(1, k+1))


def permutation(n, k):
    return product(range(n-k+1, n+1))




if __name__ == "__main__":
    pass
