# 10 hours of brute force
from number import memoize
from sympy.ntheory import n_order

@memoize
def ord10(n):
    return n_order(10, n)

def L(n):
    while n % 2 == 0: n //= 2
    while n % 5 == 0: n //= 5
    if n == 1: return 0
    return ord10(n)

s = 0
for i in range(1, 10**8):
    s += L(i)
    if i % 10000 == 1: print(i, L(i))

print(s)