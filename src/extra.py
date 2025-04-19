"""Extra functions leftover from problems or number.py"""

from number import *
    

def ternary_search(f, l, r):
    for i in range(100):
        m1 = l + (r-l) // 3
        m2 = r - (r-l) // 3
        #print(l, m1, m2, r)

        if f(m1) < f(m2):
            r = m2
        else:
            l = m1
    return (l + r) // 2

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


def partitions(n, m=1):
    """Create partitions of n.

    :param n: integer to partition
    :param m: min new value to add (for recursion)
    :return: generator of ordered partitions, e.g. [1,1,1], [1,2], [3]
    """
    if n == 0:
        yield []
        return

    for i in range(m, n+1):
        for l in partitions(n-i, i):
            yield [i] + l


def comb_mod(n, k, m):
    from number import mod_inv
    assert n >= 0
    num, den = 1, 1
    for i in range(n-k+1, n+1):
        num = (num * i) % m
    for i in range(1, k+1):
        den = (den * i) % m

    return (num * mod_inv(den, m)) % m


# this is supposed to be more efficient than char strings like "0011" but
# it's not even that much faster. for fun
from dataclasses import dataclass
@dataclass
class Bitstring:
    val: int
    nbits: int

    def __hash__(self):
        return hash((self.val, self.nbits))

    def __repr__(self):  # prettier binary string output
        s = format(self.val, 'b').zfill(self.nbits) if self.nbits else '_'
        return f"<Bitstring {s}>"


class Polynomial:
    """Polynomial represented by list of coefficients."""
    def __init__(self, l):
        self.coef = l
        self.deg = len(l) - 1

    def __str__(self):
        return " + ".join(
            f"{self.coef[d]} x^{d}" for d in range(self.deg+1))

    def __mul__(self, other):
        p, q = self, other
        r = [0] * (p.deg + q.deg + 1)
        for i in range(len(r)):
            for j in range(i+1):
                if j <= p.deg and i-j <= q.deg:
                    r[i] += p.coef[j] * q.coef[i-j]

        return Polynomial(r)

# https://stackoverflow.com/a/63552117/3163618
def ctz(v):
    if v == 0: raise ValueError
    return (v & -v).bit_length() - 1

import numpy as np
def matrix_powmod(A, k, mod):
    r = np.eye(2, dtype=np.int64)
    while k:
        if k % 2:
            r = (r @ A) % mod
        A = (A @ A) % mod
        k >>= 1

    return r


