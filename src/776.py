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
    return sum(c(s-i, d-1) * i * 10**(d-1) + D(s-i, d-1) for i in range(10))

def q(n, s):
    """Sum of values <= n with digit sum s.
    """

    digits = [int(c) for c in str(n)]
    nd = len(digits)
    w = nd-1  # wildcard digits
    old_s = s
    r = 0
    for j in range(nd):
        d = digits[j]
        for i in range(d):
            z = (n // (10**(w+1)) * 10**(w+1)) + i*(10**w)
            #print(i, s-i, w, z, c(s-i,w), D(s-i, w))
            r += z* c(s-i, w) + D(s-i, w)
        s -= d
        w -= 1

    if sum(digits) == old_s:
        r += n
    #r += D(old_s, old_s)  # n itself

    return r

def F(N):
    r = 0
    for d in range(1, 1000):
        print(d, q(N,d))
        r += q(N, d) / d
    return r

#print(q(123, 1))
#print(c(0,2))
print(f"{F(1234567890123456789):.12e}".replace("+",''))
