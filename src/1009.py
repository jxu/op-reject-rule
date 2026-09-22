from math import ceil, floor, log
from number import int_to_base, ceil_div

# max is inclusive
def f(a, b, k, n_min, n_max, a_base=0, b_base=0):
    if k == -1:
        return n_max

    res = 0

    for d in range(a-1, -1, -1):
        n_a_min = a_base + d * a**k
        n_a_max = n_a_min + a**k - 1

        n_b_min = ceil_div((b_base + d * b**k), 2)
        n_b_max = (b_base + (d+1) * b**k - 1) // 2

        # restrict interval
        new_n_min = max(n_min, n_a_min, n_b_min)
        new_n_max = min(n_max, n_a_max, n_b_max)

        if new_n_max - new_n_min < 0:
            continue 

        z = f(a, b, k-1, new_n_min, new_n_max, a_base=n_a_min, b_base=(b_base + d * b**k))
        if z != 0:
            return z

    return 0


def F(a, b):
    max_k = int(log(4) / log(b / a))
    return f(a, b, max_k, 0, a**(max_k+1) - 1)

def G(a):
    return sum(F(a, b) for b in range(a+1, 4*a))

print(sum(G(a) for a in range(2, 21)))
