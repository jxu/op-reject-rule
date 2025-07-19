from number import sieve, val_fact, mul_order, mod_inv, factor
from collections import Counter
from math import lcm, gcd

M = 10**9 + 7

def mul_order_p(a, p, k):
    """ord_p^k a"""
    # Bach and Shallit
    # keep result in factored form

    n = p**k
    
    if gcd(a, n) != 1:
        raise ValueError

    phi_n = (p**(k-1)) * (p - 1)
    factors_phi = Counter({p: k-1}) | factor(p - 1)
    #print(factors_phi)
    
    order = Counter()
    
    for qi, ei in factors_phi.items():
        yi = phi_n // (qi ** ei)
        xi = pow(a, yi, n)
        while xi != 1:
            #print(xi, order)
            xi = pow(xi, qi, n)
            order[qi] += 1

    return order
    

def R(a, n):
    primes = sieve(n)
    c = Counter()
    
    for p in primes:
        v = val_fact(p, n)
        o = mul_order_p(a, p, v)
        print(o)

        keys = c.keys() | o.keys()

        # lcm
        c = Counter({k: max(c[k], o[k]) for k in keys})
    
        #print(c)

    # get final answer
    r = 1
    for p, e in c.items():
        r = (r * pow(p, e, M)) % M

    return r

#print(val_fact(2, 10**7))
#print(mul_order_p(17, 13, 50))
#print(mul_order_p(2, 10**9 + 7, ))
print(R(10**9 + 7, 12))
