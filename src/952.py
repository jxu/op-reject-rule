from number import sieve, val_fact, mul_order, mod_inv, factor, binary_search
from collections import Counter
from math import lcm, gcd

M = 10**9 + 7

def mul_order_p(a, p, k):
    """ord_p^k a"""
    # Bach and Shallit
    # keep result in factored form
    #print(f"mul order {a} mod {p}^{k}")
    n = p**k
    
    if gcd(a, p) != 1:
        raise ValueError

    phi_n = (p**(k-1)) * (p - 1)
    factors_phi = Counter({p: k-1}) | factor(p - 1)
    #sprint(factors_phi)

    t = phi_n
    order = Counter()
    
    for pi, ei in factors_phi.items():
        #print(pi, ei)
        #t = t // pow(pi, ei)

        # binary search qi?
        yi = phi_n // (pi ** ei)
        #print("yi", yi)

        xi = pow(a, yi, n)

        def f(d):
            return pow(xi, pi**d, n) == 1

        di = binary_search(f, 0, ei) + 1

        #print("order", pi, di)
        order[pi] = di
        
        #while xi != 1:
        #    #print(order[pi])
        #    xi = pow(xi, pi, n)
        #    #t *= pi
        #    order[pi] += 1

    print("order", order)

    return order
    

def R(a, n):
    primes = sieve(n)
    c = Counter()
    
    for p in primes:
        v = val_fact(p, n)
        #print(p, "val", v)
        o = mul_order_p(a, p, v)
        print(p, v, o)

        keys = c.keys() | o.keys()

        # lcm
        c = Counter({k: max(c[k], o[k]) for k in keys})
    
        #print("final", c)

    # get final answer
    r = 1
    for p, e in c.items():
        r = (r * pow(p, e, M)) % M

    return r

#print(val_fact(2, 10**7))
#print(mul_order_p(17, 13, 50))
#print(R(10**9 + 7, 12))
print(R(10**9 + 7, 10**4))
