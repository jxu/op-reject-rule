import sys
from itertools import pairwise

sys.setrecursionlimit(11000)

def farey(a, b, c, d, n):
    """Recursively yield fractions with den <= n between a/b and c/d"""
    x, y = a + c, b + d
    if y > n: return
    # Fancy generator
    yield from farey(a, b, x, y, n)
    yield (x, y)
    yield from farey(x, y, c, d, n)

def f(n):
    yield (0, 1)
    yield from farey(0, 1, 1, 1, n)
    yield (1, 1)

def F(N):
    s = 0
    for f1, f2 in pairwise(f(N)):
        a, b = f1
        c, d = f2
        s += (c/d - a/b)**2 * b / 2

    return s

print(round(F(10000), 13))

