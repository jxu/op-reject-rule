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
def q(n, s):
    """Sum of values <= n with digit sum s."""
    if n < 0: return 0
    ns = sum(int(c) for c in str(n))  # n digit-sum
    w = 0  # wildcard spaces
    r = 0
    if ns == s: r += n  # consider original n

    # go digit-by-digit left (original code went right)
    # e.g. for n = 123, consider 123,
    # 122, 121, 120, 11x, 10x, 0xx
    while n:
        for i in range(n % 10):
            n -= 1
            ns -= 1
            # idea from jakob223: recurse using q instead of
            # D(s,d) = q(10**d - 1, s)
            # e.g. for 12**, add sum of 2-digits with digit-sum s,
            # plus 1200 * how many 2-digits with digit-sum s
            r += n * 10**w * c(s-ns, w) + q(10**w - 1, s-ns)

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
