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



p = Polynomial([1,1,1])
q = Polynomial([1,1])
print(p * q)