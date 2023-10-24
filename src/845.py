from number import sieve, binary_search
from functools import cache

primes = sieve(1000)

@cache
def c(s, d):
    """Count integers with d digits and s digit-sum with DP"""
    if s < 0: return 0
    assert d >= 0
    if d == 0: return int(s == 0)
    return sum(c(s-i, d-1) for i in range(10))


def q(n, s):
    """Count values <= n with digit sum s.

    go digit by digit, ex for n = 333, consider
    333
    332 331 330
    32* 31* 30*
    2** 1** 0**

    adamant idea: first find out how many digits the answer has, then
    recover the answer one digit at a time (no binary search needed)
    """
    r = 0
    n += 1  # handles n itself in below loop
    ns = sum(int(d) for d in str(n))  # n digit-sum
    w = 0
    while n:
        for i in range(n%10):
            ns -= 1
            r += c(s-ns, w)
        w += 1
        n //= 10

    return r


def d(n):
    """Left inverse of D: Count how many integers <= n have prime digit-sum"""
    return sum(q(n, p) for p in primes)


print(binary_search(lambda n: d(n) >= 10**16, 0, 10**20) + 1)