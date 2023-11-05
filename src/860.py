from number import comb_mod, mod_inv
m = 989898989


def fact_mod_list(n, m):
    """Compute [0!, ..., n!] mod m in O(n)."""
    fact_mod = [1] * (n + 1)
    for i in range(2, n+1):
        fact_mod[i] = (i * fact_mod[i-1]) % m
    return fact_mod

def inv_list(l, m):
    return list(map(lambda x: mod_inv(x,m), l))


def F(n):
    n //= 2  # makes math a little nicer
    fact_mod = fact_mod_list(2*n, m)
    fact_inv = inv_list(fact_mod, m)

    s = 0
    for i in range (0, n//5+1):
        for j in range((n-5*i) + 1):
            k = (n - 5*i - j)
            assert 2*j + 2*k + 10*i == 2*n
            r = (1 + (i > 0))
            for t in (fact_mod[2*n], fact_inv[j], fact_inv[j+2*i],
                      fact_inv[k], fact_inv[k+8*i]):
                r = (r * t) % m
            s = (s + r) % m

    return s


print(F(9898))