from math import comb, factorial
from number import comb_mod, mod_inv
from functools import cache
import sys
sys.setrecursionlimit(20000)
m = 989898989

@cache
def fact_mod(n, m):
    assert n >= 0
    if n == 0: return 1
    return (n * fact_mod(n-1, m)) % m

@cache
def fact_inv(n, m):
    return mod_inv(fact_mod(n, m), m)

def F(n):
    n //= 2
    s = 0
    for i in range (0, n//5+1):
        for j in range((n-5*i) + 1):
            k = (n - 5*i - j)
            assert 2*j + 2*k + 10*i == 2*n
            #print(i,j,k, 2*j + 2*k + 10*i)
            s = (s + 2* (fact_mod(2*n, m) *
                   fact_inv(j, m) *
                   fact_inv(j+2*i,m) *
                   fact_inv(k+8*i, m) *
                   fact_inv(k, m)) % m)


    for j in range(n+1):
        k = n-j
        s = (s - fact_mod(2*n, m) * (fact_inv(j,m) * fact_inv(k,m))**2) % m


    return s % m

for n in range(10000):
    fact_mod(n,m)


print(F(2))
print(F(10))
print(F(9898))