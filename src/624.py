"""Two heads are better than one

M=2: HH          Pr(M=2) = 1/4
M=3: THH         Pr(M=3) = 1/8
M=4: XTHH        Pr(M=4) = 2/16
M=5: XXTHH       Pr(M=5) = 3/32
M=6: XXXTHH      Pr(M=6) = 5/64
                 Pr(M)   = F_{M-1} / 2^M

XXX is a string of tosses without two heads in a row.
The recurrence also comes from every such string being of the form
XXXT or XXXTH, where XXX is a shorter such string.
Let f(n) count such strings of length n, then f(n) = f(n-1) + f(n-2).

There are F_{M-1} possible strings.

Every nth probability has n|M. The sum is 

P(n) = sum_{k=1..inf} F_{kn-1} / 2^n

can be computed directly with Binet's formula or with generating functions.
See notebook for derivation with phi and psi. The closed form is

P(n) = (2^n F_{n-1} + (-1)^{n-1}) / (4^n - 2^n L_n + (-1)^n)

Finally, a = bq (mod p) <=> a b^-1 = q (mod p), so a and b are computed mod p.
"""
from number import cache, mod_inv

# Probably can go in number functions
@cache
def fibmod(n, m):
    """F_n mod m for huge n.

    Uses doubling formulas:
    F_2n = F_n (2 F_{n+1} - F_n)
    F_{2n+1} = F_{n+1}^2 + F_n^2
    """
    if n <= 1: return n 
    if n == 2: return 1

    fh = fibmod(n//2, m)
    fh1 = fibmod(n//2 + 1, m)
    
    if n % 2 == 0:
        return (fh * (2 * fh1 - fh)) % m
    else:
        return (fh1**2 + fh**2) % m


def lucasmod(n, m):
    if n == 0: return 2
    return (fibmod(n+1, m) + fibmod(n-1, m)) % m


def Q(n, p):
    a = pow(2, n, p) * fibmod(n-1, p) + (-1)**(n-1)
    b = pow(4, n, p) - pow(2, n, p)*lucasmod(n, p) + (-1)**n

    return (a % p) * mod_inv(b, p) % p

print(Q(10**18, 10**9 + 9))
