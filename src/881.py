# Let n = p1^e1 p2^e2 ... pj^ej.
# For level k (numbering levels from the bottom up),
# the width of the graph is # solutions to
# a1 + ... + aj = k, with a1 <= e1, ..., aj <= ej.
# With generating functions this is simply the coefficient of x^k in
# (1 + x + x^2 + ... + x^e1) ... (1 + x + x^2 + ... + x^ej)
# and g(n) is the maximum coefficient of the resulting polynomial.
# (Here I implemented a simple Polynomial class with polynomial multiplication,
# but j... suggests optimizing multiplication by 1 + x + x^2 + ...
# in linear time.)

# To actually find minimal n, I use a Dijkstra-like search of the solution
# space I came up with while not being able to fall asleep last night.
# Start with node n = 2 and list of prime exponents [1],
# as long as e1 >= e2 >= ..., we can increase the last power or introduce
# a new prime. This way the search won't revisit any n.
# The min-heap has key n, and the search ends when n has g(n) >= 1000.

from number import sieve
from heapq import *

primes = sieve(100)

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


def g(exponents):
    q = Polynomial([1])
    for e in exponents:
        q *= Polynomial([1] * (e+1))  # math.prod wants SupportsIndex
    return max(q.coef)

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

