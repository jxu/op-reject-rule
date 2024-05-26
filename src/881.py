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
        q *= Polynomial([1] * (e+1))
    return max(q.coef)

h = [(2, [1])]
best_g, best_n = 0, 0
for _ in range(10**6):
    n, e = heappop(h)
    gn = g(e)
    if gn > best_g:
        best_g = gn
        best_n = n
        print(n, gn)

    if gn >= 10**4:
        print(n)
        break


    last_e = len(e) - 1

    n1 = n * primes[last_e]
    f1 = e.copy()
    f1[last_e] += 1
    heappush(h, (n1, f1))

    n2 = n * primes[last_e+1]
    f2 = e.copy()
    f2.append(1)
    heappush(h, (n2, f2))

