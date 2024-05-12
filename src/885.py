# Uninteresting brute force on possible ascending digit nums
# See solution thread for constant-time solution!
from number import fact_mod_list, inv_list

M = 1123455689

def g(max_d, digits_left):
    if not digits_left:
        yield 0; return

    for d in range(max_d+1):
        for s in g(d, digits_left-1):
            # build right-to-left. faster than string ops
            yield 10*s + d


def S(n):
    fact_mod = fact_mod_list(n, M)
    fact_inv = inv_list(fact_mod, M)

    r = 0
    for m in g(9, n):
        s = str(m).zfill(n)
        x = fact_mod[n]
        for d in range(10):
            x = (x * fact_inv[s.count(str(d))]) % M

        r = (r + m * x) % M

    return r

print(S(18))