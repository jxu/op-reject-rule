"""Brute force on sum-of-two-squares  

80 mins
"""

from number import factor, sieve


def r2(n, primes):
    """Sum of two squares function via Jacobi's two-square theorem"""
    r = 4
    for p, e in factor(n, primes).items():
        if p == 2: continue
        if p % 4 == 1: 
            r *= e + 1
        if p % 4 == 3 and e % 2 == 1:
            return 0 


    return r 

def d2(n, primes):
    return r2(8*n + 2, primes) // 4


def G(n):

    primes = sieve(int((8*n+2)**0.5))


    s = 0
    for c in range(n):
        t = c*(c+1)//2
        if n - t < 0: break
        
        r = d2(n - t, primes)
        print(n - t, r)
        s += r

    return s

#print(G(10**6))
print(G(17526 * 10**9))
