from number import sieve, val_fact, linear_sieve, linear_sieve_factors
from collections import Counter


def mul_order_p(a: int, p: int, factors_p1: Counter[int]) -> \
    tuple[int, Counter[int]]:
    """Computes order of a mod p, given factorization of p-1

    From Handbook of Applied Cryptography
    Keeps result in factored form for space efficiency
    """
    order = Counter()
    t = p - 1
    
    for pi, ei in factors_p1.items():
        t //= (pi ** ei)
        a1 = pow(a, t, p)

        while a1 != 1:
            a1 = pow(a1, pi, p)
            t *= pi
            order[pi] += 1

    return t, order


def mul_order_pk(a: int, p: int, k: int, factor_p1: Counter[int]) -> \
    Counter[int]:
    """Compute order of a mod p^k for large k by trying small powers

    p must be odd. Keeps order in factored form.

    Idea is hope we can lift the exponent:
    ord_{p^k}(a) = ord_{p^{k-1}}(a) or p times that

    Usefully, if p | ord_{p^k}(a), then ord_{p^{k+1}}(a) = p * ord_{p^k}(a)
    and we can apply this all the way up the powers

    https://math.stackexchange.com/a/4751948
    """
    if p < 3: raise ValueError

    t, o = mul_order_p(a, p, factor_p1)

    for j in range(2, k+1):
        if p in o:
            # lifting-the-exponent
            # if p divides order, then order mod p^(k+1) = p * order mod p^k
            # apply this all the way from j to k
            o[p] += k - j + 1
            break
        else:
            if pow(a, t, p**j) != 1:
                # t not sufficient, so must be p*t 
                o[p] += 1
    
    return o


def R(a, n, M = 10**9 + 7):
    primes = sieve(n)  # primes in n!
    c = Counter()
    lp = linear_sieve(n) 
   
    # compute order for p^k making up n!
    for p in primes:
        v = val_fact(p, n)  # power of p in n!
        if p == 2:  
            # special case for this a and k >= 4: 
            # order mod 2^k = 2^(k-3), by induction or LTE
            o = Counter({2: v-3})
        
        else:
            lf = linear_sieve_factors(lp, p-1)
            o = mul_order_pk(a, p, v, lf)
       
        # lcm property: order mod mn = lcm(order mod m, order mod n)
        for k in o:
            c[k] = max(c[k], o[k])
    
    # compute final product
    r = 1
    for p, e in c.items():
        r = (r * pow(p, e, M)) % M

    return r

print(R(10**9 + 7, 10**7))
