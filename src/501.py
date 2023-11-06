# Ran for 3 minutes until memory error from caching prime count values... this really isn't a task for python

from number import sieve, memoize

def test_prime_count():
    # A000720
    small_values = (0,0,1,2,2,3,3,4,4,4,4,5,5,6,6,6,6,7,7,8,8)
    for i in range(len(small_values)):
        assert prime_count(i) == small_values[i]

    # A006880
    powers_10 = (0, 4, 25, 168, 1229, 9592, 78498, 664579)

    for i in range(len(powers_10)):
        assert prime_count(10**i) == powers_10[i]


# TODO: clean up prime counting function
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


def f(n):
    primes = sieve(int(n**0.5))

    # Case 1: n = p^7
    count = prime_count(int(n**(1/7)))

    # Case 2: n = p^3 * q
    for p in primes:
        if p**3 > n: break
        q_max = n // (p**3)
        # Exclude case with p == q
        count += prime_count(q_max) - (q_max >= p)

    print("Starting case 3...")
    # Case 3: n = p*q*r, p < q < r
    for p_i in range(len(primes)):
        p = primes[p_i]
        if p**3 > n: break

        for q_i in range(p_i + 1, len(primes)):
            q = primes[q_i]
            if q > (n / p)**0.5: break  # max q when q = r so n = p * q^2
            print(p, q, n//(p*q))

            # q < r < n/pq, so add pi(n/pq) - pi(q)
            count += prime_count(n // (p*q)) - (q_i + 1)

    return count


print(f(10**12))