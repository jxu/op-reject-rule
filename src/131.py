# Derivations (mathblog.dk)
# n^3 + n^2p = k^3  <=>  n cbrt(p + n) / cbrt(n) = k
# n = x^3, p + n = y^3;  p = y^3 - x^3 = (y-x)(y^2 + yx + x^2)
# Since p has 2 factors, y-x = 1
# (i+1)^3 - i^3 < 1000000, i < 577
from number import is_prime
print(sum(is_prime((i+1)**3 - i**3) for i in range(1, 577)))