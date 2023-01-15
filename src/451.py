# Finding largest squareroot of 1 mod n, != -1 mod n
# By Chinese Remainder Theorem, x^2 = 1 mod n can be determined uniquely by
# x^2 = 1 mod p1^e1, = 1 mod p2^e2, ...
# For odd p, it can be shown the only sols for x^2 = 1 mod p^e are +-1
# For p = 2, the squareroots for e >= 3 are +-1 and 2^(e-1) +- 1
# https://math.stackexchange.com/q/2693243
# So try all combinations of squareroots for prime powers and combine with CRT
# (I(n) given by A284254)

from number import linear_sieve, factors_from_linear_sieve, memoize, \
    extended_euclidean, crt
from itertools import product

lp = linear_sieve(2 * 10**7)

@memoize
def crt_memo(rs, mods):
    """Chinese Remainder Theorem for x = r[i] mod m[i]

    Solve for x = r mod m1*m2*...
    Exact solution from Wikipedia
    """
    r0, m0 = rs[0], mods[0]
    if len(rs) == 1:
        return r0 % m0, m0

    r1, m1 = rs[i], mods[i]
    g, n0, n1 = extended_euclidean(m0, m1)


    for i in range(1, len(mods)):

        x = (r0*n1*m1 + r1*n0*m0) % (m0*m1)
        r0, m0 = x, m0*m1

    return r0 % m0, m0

def I(n):
    pp = factors_from_linear_sieve(lp, n)
    rs_list = []
    ms = [p**e for p,e in pp.items()]

    il = []

    # save intermediate CRT results
    def dfs(ps, es, ms, cur_r=0, cur_m=1):
        #print(ps, es, ms, cur_r, cur_m)

        if len(ps) == 0:
            i = cur_r % cur_m
            if i != cur_m - 1:
                #print(i)
                il.append(i)
            return

        p, e = ps[0], es[0]
        m = ms[0]


        if p == 2:
            if e == 1:
                rs = (1,)
            elif e == 2:
                rs = (1, -1)
            else:
                rs = (1, -1, 2 ** (e - 1) + 1, 2 ** (e - 1) - 1)
        else:
            rs = (1, -1)

        for r in rs:
            new_r, new_m = crt([cur_r, r], [cur_m, m])
            dfs(ps[1:], es[1:], ms[1:], new_r, new_m)



    ps = list(pp.keys())
    es = list(pp.values())
    dfs(ps, es, ms)

    return max(il)

#print(I(100))

print(sum(I(n) for n in range(3, 2 * 10**6 + 1)))
