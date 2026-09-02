# Exponential generating function idea
# 18th coef of (x^0/0! + x^1/1! + x^2/2! + x^3/3!)^10
R.<x> = PolynomialRing(QQ)

p = 1 + x + x^2/2 + x^3/6

print((9/10) * factorial(18) * (p^10)[18])
