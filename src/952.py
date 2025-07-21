from number import sieve, val_fact, mul_order, mod_inv, factor, linear_sieve, linear_sieve_factors
from collections import Counter
from math import lcm, gcd, prod

def factors_prod(c: Counter) -> int:
    return prod(p**e for p, e in c.items())


def mul_order_p(a, p, factors_p1):
    """Computes order of a mod p, given factorization of p-1

    From Bach & Shallit, Algorithmic Number Theory
    Keeps result in factored form for space efficiency
    """
    order = Counter()
    
    for pi, ei in factors_p1.items():
        yi = (p-1) // (pi ** ei)
        xi = pow(a, yi, p)

        while xi != 1:
            xi = pow(xi, pi, p)
            order[pi] += 1

    return order


def lte(a, p, k, factor_p1):
    if p < 3: raise ValueError

    j = 1
    o = mul_order_p(a, p, factor_p1)
    on = factors_prod(o)

    for j in range(2, k+1):
        if p in o:
            # lifting-the-exponent
            # if p divides order, then order mod p^(k+1) = p * order mod p^k
            o[p] += k - j + 1
            break
        else:
            if pow(a, on, p**j) == 1:
                pass
            else:
                o[p] += 1
                on *= p

    return o

def R(a, n, M = 10**9 + 7):
    primes = sieve(n)
    c = Counter()
    lp = linear_sieve(n) 
    
    for p in primes:
        v = val_fact(p, n)
        if p == 2:  
            # special case for this a and k >= 4: 
            # order mod 2^k = 2^(k-3), by induction or LTE
            o = Counter({2: v-3})
        
        else:
            o = lte(a, p, v, linear_sieve_factors(lp, p-1))
       
        # lcm
        for k in o:
            c[k] = max(c[k], o[k])
    
    # get final product
    r = 1
    for p, e in c.items():
        r = (r * pow(p, e, M)) % M

    return r

print(R(10**9 + 7, 10**7))
