# IMO 1995 Problem 6 (thanks to my friend John for pointing this out)
# Generating function approach with roots-of-unity filter described in
# http://zacharyabel.com/papers/Multi-GF_A06_MathRefl.pdf
# Timing (ThinkPad) with mul_inv for all n
#   Python 3.6: 10m 25s, PyPy 5.10.0: 1m 37s
# Save lots of computation by using fractions mod M and calculate mul_inv at end
# New timings with ModFraction
#   Python 3.6: 5m 59s, PyPy 5.10.0: 13.5s


from number import sieve, mod_inv
M = 1000000009
L = 10**8
sp = set(sieve(L))


class ModFraction:
    """Fraction with numerator and denominator mod p. Mod must be prime"""
    def __init__(self, num, den, mod):
        self.num = num % mod
        self.den = den % mod
        self.mod = mod

    def __repr__(self):
        return "<ModFraction {}/{} mod {}>".format(
            self.num, self.den, self.mod)

    def __add__(self, other):
        new_num = self.num * other.den + other.num * self.den
        new_den = self.den * other.den
        return ModFraction(new_num, new_den, self.mod)

    def __mul__(self, other):
        new_num = self.num * other.num
        new_den = self.den * other.den
        return ModFraction(new_num, new_den, self.mod)

    def calc(self):
        return (self.num * mod_inv(self.den, self.mod)) % self.mod


A2 = ModFraction(-2, 1, M)  # adjust for A2(2) = 2 instead of 4
A3 = ModFraction(-3, 1, M)  # A3(2) = 6 instead of 9
bin2 = ModFraction(1, 1, M) # (2n choose n)
bin3 = ModFraction(1, 1, M) # (3n choose n)

for n in range(L - 1):
    if n in sp:
        p = n  # prime
        A2 = A2 + ModFraction(1, p, M) * (bin2 + ModFraction(2*(p-1), 1, M))
        A3 = A3 + ModFraction(1, p, M) * (bin3 + ModFraction(3*(p-1), 1, M))

    bin2 = bin2 * ModFraction(4*n + 2, n + 1, M)
    bin3 = bin3 * ModFraction(3*(3*n+1)*(3*n+2), (2*n+1)*(2*n+2), M)

print(A2.calc(), A3.calc())
print((A2.calc() + A3.calc()) % M)
