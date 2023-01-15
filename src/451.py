from number import linear_sieve, factors_from_linear_sieve, crt
from itertools import product

lp = linear_sieve(2 * 10**7)

def I(n):
    pp = factors_from_linear_sieve(lp, n)
    rs_list = []
    ms = [p**e for p,e in pp.items()]
    for p, e in pp.items():
        m = p ** e
        if p == 2:
            rs = (1, -1, 2**(e-1) + 1, 2**(e-1) - 1)
            rs = list(set(r % m for r in rs))
        else:
            rs = (1, -1)
        rs_list.append(rs)

    max_r = 0
    for rs in product(*rs_list):
        r, m = crt(rs, ms)
        if (r % m) != m-1:
            max_r = max(max_r, r)

    return max_r

s = 0
for n in range(3, 2 * 10**7 + 1):
    i = I(n)
    print(n, i)
    s += i

print(s)