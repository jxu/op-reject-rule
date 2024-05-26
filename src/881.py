from number import factor, sieve

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

def g(factors):
    #factors = factor(n)


    q = Polynomial([1])

    for p, e in factors.items():
        q *= Polynomial([1] * (e+1))

    return max(q.coef)

step = 2 * 2 * 3 * 5 * 7 * 11 * 13

best_n, best_g = 0, 0
for n in range(step, 10**10, step):
    factors = factor(n)
    z = False
    for i in range(1, len(primes)):
        if factors[primes[i]] > factors[primes[i-1]]:
            z = True
            break
        if primes[i] > max(factors.keys()): break

    if z: continue

    gn = g(factors)
    if gn > best_g:
        best_n = n
        best_g = gn
        print(n, gn)


