# same idea as #845: go digit by digit for <= N
from functools import cache

@cache
def c(s, d):
    """Count integers with d digits and s digit-sum"""
    if s < 0: return 0
    assert d >= 0
    if d == 0: return int(s == 0)
    return sum(c(s-i, d-1) for i in range(10))

@cache
def D(s,d):
    """Sum of integers with d digits and s digit-sum"""
    if s <= 0: return 0
    if d == 0: return 0
    assert d >= 0
    return sum(i * c(s-i, d-1) * 10**(d-1) + D(s-i, d-1) for i in range(10))

def q(n, s):
    """Sum of values <= n with digit sum s."""
    ns = sum(int(c) for c in str(n))  # n digit-sum
    w = 0  # wildcard spaces
    r = 0
    if ns == s: r += n  # consider original n

    # go digit-by-digit left (original code went right)
    while n:
        last_digit = n % 10
        for i in range(last_digit):
            n -= 1
            ns -= 1
            # add wildcard sum + contribution from rest of digits
            r += (n) * 10**w * c(s-ns, w) + D(s-ns, w)
            #print(n, n * 10**w, s-ns, w, c(ns,w))

        n //= 10
        w += 1

    return r

def F(N):
    r = 0
    for d in range(1, 200):
        print(d, q(N,d)/d)
        r += q(N, d) / d
    return r

print(f"{F(1234567890123456789):.12e}".replace("+",''))
