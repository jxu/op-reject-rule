# Nice sublinear problem idea.

# gcdsum(j) = Sum_{i=1..j} gcd(i, j) = Sum_{d|j} d * phi(j/d)
# because d = gcd(i, j) exactly when d|i and d|j and gcd(i/d, j/d) = 1
# so there are phi(j/d) terms of d
# As gcdsum = Id (Dirichlet convolution) phi
# f = Id, g = phi, summatory functions F = T, G = Phi
# Apply the O(n^3/4) Dirichlet hyperbola method directly to gcdsum:
# Sum_{j=1..n} gcdsum(j) =
# Sum_{i<=sqrt n} f(i) G(n/i) + Sum_{j<=sqrt n} g(j) F(n/j)
# - F(sqrt n) * G(sqrt n)

from number import totient_sum


def T(n):
    return n * (n + 1) // 2

# use hyperbola method instead of floor counting
# totients and totient sums calculated before
def G(N):
    s = 0
    isqrt = int(N**0.5)  # fixed
    for i in range(1, isqrt+1):
        s += i * totient_sum(N // i)

    for j in range(1, isqrt+1):
        s += totient_sum(j) * T(N // j)

    s -= T(isqrt) * totient_sum(isqrt)

    return s

print(G(10**11) % 998244353)
