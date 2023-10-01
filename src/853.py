# Fibonacci residues mod n cycles begin 0, 1, ...
# Check F_120 = 0 mod n, F_121 = 1 mod n
# => n | gcd(F_120, F_121 - 1)
# Then ensure period isn't a proper divisor of 120

from number import fib_list, divisors, factor
from math import gcd

F = fib_list(121)

def f(pi_n, limit):
    s = 0
    g = gcd(F[pi_n], F[pi_n+1]-1)
    for n in sorted(divisors(factor(g))):
        if n >= limit: break
        if all((F[m]%n, F[m+1]%n) != (0,1) for m in range(1, pi_n)):
            print(n)
            s += n
    return s

print(f(120, 10**9))