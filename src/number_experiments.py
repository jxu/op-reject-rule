def sieve_factor(n):
    fact = [[] for _ in range(n)]
    for i in range(2, n):
        if fact[i] == []:
            j = i
            while j <= n:
                for k in range(j, n, j):
                    fact[k].append(i)
                j *= i

    return fact


from number import extended_euclidean
def crt_recursive(rs, mods):
    """Chinese Remainder Theorem for x = r[i] mod m[i]

    Returns solution (r, m) of x = r mod m, with m = m1*m2*...
    Exact solution from Wikipedia
    """
    print(rs, mods)
    r0, m0 = rs[-1], mods[-1]
    if len(rs) == 1:
        return r0 % m0, m0

    r1, m1 = rs[-2], mods[-2]
    g, n0, n1 = extended_euclidean(m0, m1)
    r = (r0*n1*m1 + r1*n0*m0) % (m0*m1)
    m = m0 * m1

    rs = rs[:-2] + [r]  # ugly list slicing
    mods = mods[:-2] + [m]
    return crt_recursive(rs, mods)

assert crt_recursive([2, 3], [3, 5]) == (8, 15)