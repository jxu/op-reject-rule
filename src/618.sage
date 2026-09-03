# (A002098) G.f. approach is
# Product_p ((p x^p)^0 + (p x^p)^1 + (p x^p)^2 + ...)
# = Product_p 1 / (1 - p x^p)
# Sage lets us work directly in (Z / 10^9 Z)[[x]], which does mod for us

N = fibonacci(24)

R.<x> = PowerSeriesRing(Zmod(10^9), default_prec=N+1)

g = prod(1 / (1 - p * x^p) for p in prime_range(N+1))

print(sum(g[fibonacci(k)] for k in range(2, 25)))
