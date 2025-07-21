from number import sieve, val_fact, mul_order, mod_inv, factor, linear_sieve, linear_sieve_factors
from collections import Counter
from math import lcm, gcd, prod

M = 10**9 + 7

def mul_order_pk(a, p, k):
    """ord_p^k a"""
    # Bach and Shallit
    # keep result in factored form
    #print(f"mul order {a} mod {p}^{k}")
    n = p**k
    
    if gcd(a, p) != 1:
        raise ValueError

    phi_n = (p**(k-1)) * (p - 1)
    factors_phi = Counter({p: k-1}) | factor(p - 1)

    order = Counter()
    
    for pi, ei in factors_phi.items():
        yi = phi_n // (pi ** ei)
        xi = pow(a, yi, n)

        while xi != 1:
            xi = pow(xi, pi, n)
            order[pi] += 1

    return order

def factors_prod(c: Counter) -> int:
    return prod(p**e for p, e in c.items())


def mul_order_p(a, p, factors_phi):
    """ord_p a"""
    # keep result in factored form

    order = Counter()
    
    for pi, ei in factors_phi.items():
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
            o[p] += k - j + 1
            break
        else:
            if pow(a, on, p**j) == 1:
                pass
            else:
                o[p] += 1
                on *= p

    return o

def R(a, n):
    primes = sieve(n)
    c = Counter()
    lp = linear_sieve(n) 
    
    for p in primes:
        # test certain p
        v = val_fact(p, n)
        #print(p, "val", v)

        #w = 1

        # somehow use for odd p, ord_p^k a = p * ord_p^(k-1) a
        # p = 2 case? 
        # if p | ord_p^(k-1) a
        #for w in range(1, 100):
        #    print(w, mul_order_p(a,p,w))

        if p == 2:
            # by induction
            assert (a % 32) == 7 and v >= 4
            o = Counter({2: v-3})
        
        else:
            o = lte(a, p, v, linear_sieve_factors(lp, p-1))
       
        if p % 100 == 1:
            print(p, v, o)

        keys = c.keys() | o.keys()

        # lcm
        c = Counter({k: max(c[k], o[k]) for k in keys})
    
        #print("final", c)

        #break  # TESTING p = 2

    # get final answer
    r = 1
    for p, e in c.items():
        r = (r * pow(p, e, M)) % M

    return r

#print(val_fact(2, 10**7))
#print(mul_order_p(10**9+7, 2, 9995))
#print(R(10**9 + 7, 12))
print(R(10**9 + 7, 10**7))
