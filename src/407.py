# Almost identical to Problem 451
# Don't need to consider p = 2 case separately

from number import linear_sieve, factors_from_linear_sieve, crt
from itertools import product

lp = linear_sieve(10**7)

def M(n):
    pp = factors_from_linear_sieve(lp, n)
    ms = [p**e for p,e in pp.items()]
    rs_list = [(0,1)] * len(pp)

    max_r = 0
    for rs in product(*rs_list):
        r, m = crt(rs, ms)
        max_r = max(max_r, r)

    return max_r

# M(1) = 0
print(sum(M(n) for n in range(2, 10**7 + 1)))
