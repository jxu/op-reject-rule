# Let n = p1^e1 p2^e2 ... pj^ej. For level k (numbering levels bottom up),
# the width of the graph is # solutions to
# a1 + ... + aj = k, with a1 <= e1, ..., aj <= ej.
# With generating functions this is simply the coefficient of x^k in
# (1 + x + x^2 + ... + x^e1) ... (1 + x + x^2 + ... + x^ej)
# and g(n) is the maximum coefficient of the resulting polynomial.

# To actually find minimal n, I use a Dijkstra-like search of the solution
# space I came up with while not being able to fall asleep last night.
# Start with node n = 2 and list of prime exponents [1],
# as long as e1 >= e2 >= ..., we can increase the last power or introduce
# a new prime. This way the search won't revisit any n.
# The min-heap has key n, and the search ends when n has g(n) >= 1000.

from number import sieve
from heapq import *
from functools import reduce

primes = sieve(100)


# optimization idea by j...
def mul1s(a, deg1):
    """Multiply polynomial a by 1 + x + x^2 + ... + x^deg1 in linear time."""
    dega = len(a) - 1
    y = a + [0] * deg1

    for  i in range(dega + deg1 + 1):
        y[i] += y[i-1]  # y[-1] is fine
        if i > deg1: y[i] -= a[i - deg1 - 1]

    return y


def g(exps):
    """Multiply polynomials (1 + x + ... + x^ei)"""
    return max(reduce(mul1s, exps, [1]))


h = [(2, [1])]

while True:
    n, e = heappop(h)
    if g(e) >= 10**4:
        print(n)
        break

    last_e = len(e) - 1
    if len(e) == 1 or e[-1] < e[-2]:
        n1, e1 = n * primes[last_e], e[:-1] + [e[-1]+1]
        heappush(h, (n1, e1))

    n2, e2 = n * primes[last_e+1], e + [1]
    heappush(h, (n2, e2))

