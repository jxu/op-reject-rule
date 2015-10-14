# Unique solutions n = abd, with gcd(a, b) = 1 (MSE)
# From mathblog.dk: Solution (d(n^2) + 1)//2 > 1000 => d(n^2) > 1999
# Divisors formula: for n = p1^a1 * p2^a2 * ... d(n) = (a1 + 1)(a2 + 1)...
# For n^2, d(n^2) = (2*a1 + 1)(2*a2 + 1)...
# Solutions are very composite numbers (ex. 2^2 * 3 * 5 * 7)
# For now, manually creating very composite numbers is enough
from itertools import product

small_primes = (2, 3, 5, 7, 11, 13, 17)
least_n = 2*3*5*7*11*13*17
for pow_list in product(range(5), repeat=7):
    d = 1
    for a in pow_list:
        d *= 2*a + 1
    if d > 1999:
        n = 1
        for i in range(len(pow_list)):
            n *= small_primes[i] ** pow_list[i]
        least_n = min(least_n, n)

print(least_n)
