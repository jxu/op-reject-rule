"""Classical problem; No OEIS cheating! 

Uses Jacobi's four-square theorem, as described in
"Grosswald (1985). Representations of integers as sums of squares"

r4(n) = 8 * Sum_{d|n, d != 0 mod 4} d 
      = 8 * (Sum_{d|n} d - Sum_{d|n,4|d} d)

Let n = 4n', d = 4d'. Since d'|n' <=> 4d'|4n', the 2nd sum is 4 Sum_{d'|n'} d'
r4(n) = 8 * (sigma(n) - 4*sigma(n/4))

A024916: Sum_{i<=n} sigma(i) with the usual Dirichlet hyperbola method.

Here sigma = Id * 1. Take f = Id, F = tri, g = 1, G = Id.

T(r) = 1 + Sum_{n<=r^2} r4(n) (+1 for origin (0,0,0,0))
"""


def hyperbola_method(n, f, F, g, G):
    """Dirichlet hyperbola method for Sum_{i<=n} (f * g)(i).
     
    = Sum_{i<=s} f(i) G(n/i) + Sum_{j<=s} g(j) F(n/j) - F(s) G(s)
    where F, G are summatory functions of f, g. s = sqrt(n)
    """
    s = int(n**0.5)
    r = 0
    for i in range(1, s+1):
        r += f(i) * G(n//i) + g(i) * F(n//i) 
    return r - F(s) * G(s)


Id  = lambda n: n
tri = lambda n: n * (n+1) // 2
one = lambda n: 1

def sum_sigma(n):
    return hyperbola_method(n, Id, tri, one, Id)

def T(r):
    return 8 * (sum_sigma(r**2) - 4 * sum_sigma(r**2 // 4)) + 1

print(T(10**8) % (10**9 + 7))
