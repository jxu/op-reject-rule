from number import sieve
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

    go digit by digit, ex for n = 4321, consider
    0xxx 40xx 430x 4320
    1xxx 41xx 431x 4321
    2xxx 42xx
    3xxx

    Another option is first find out how many digits the answer has, then
    recover the answer one digit at a time (no binary search needed)
    """

    digits = [int(c) for c in str(n)]
    nd = len(digits)-1
    old_s = s
    r = 0
    for i in range(len(digits)):
        d = digits[i]
        for i in range(d):
            r += c(s-i, nd)
            #print(d, i, s-i, nd, c(s-i, nd))
        s -= d
        nd -= 1
    r += int(sum(digits) == old_s)  # consider n itself

    return r

def d(n):
    """Left inverse of D: Count how many integers <= n have prime digit-sum"""
    return sum(q(n, p) for p in primes)

def binary_search(f, l, r):
    """Return L s.t. f(L)=0, f(L+1)=f(R)=1, if it exists"""
    while r - l > 1:
        print(l, r)
        m = (l + r) // 2
        print(m, d(m))
        if f(m): r = m
        else: l = m

    return l

# binary search input d(n)
print(binary_search(lambda n: d(n) >= 10**16,0, 10**20)+1)