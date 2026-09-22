from math import ceil, floor, log
from number import int_to_base, ceil_div

# max is inclusive
def f(a, b, k, n_min, n_max, a_base=0, b_base=0):
    #print(k, n_min, n_max, a_base, b_base)
    assert n_max - n_min >= 0

    if k == -1:
        
        #print(f"end [{n_min},{n_max})")
        print(n_max, int_to_base(n_max, a), int_to_base(2*n_max, b))
        assert int_to_base(n_max, a) == int_to_base(2*n_max, b)

        return n_max

    res = 0

    for d in range(a):
        n_a_min = a_base + d * a**k
        n_a_max = n_a_min + a**k - 1


        n_b_min = ceil_div((b_base + d * b**k), 2)
        n_b_max = (b_base + (d+1) * b**k - 1) // 2

        if not 2 * n_b_max <= b_base + (d+1) * b**k - 1:
            n_b_max -= 1

        print(int_to_base(2 * n_b_max, b), int_to_base(b_base + (d+1) * b**k - 1, b))
        assert 2 * n_b_min >= b_base + d * b**k
        assert 2 * n_b_max <= b_base + (d+1) * b**k - 1

        #print(d)
        #print(n_a_min, n_a_max, n_b_min, n_b_max)

        # restrict interval
        new_n_min = max(n_min, n_a_min, n_b_min)
        new_n_max = min(n_max, n_a_max, n_b_max)

        if new_n_max - new_n_min < 0:
            continue 


        res = max(res, f(a, b, k-1, new_n_min, new_n_max, a_base=n_a_min, b_base=(b_base + d * b**k)))

    return res


def F(a, b):
    max_k = int(log(4) / log(b / a))
    #print("max_k", max_k)
    return f(a, b, max_k, 0, a**(max_k+1) - 1)

def G(a):
    s = 0
    for b in range(a+1, 4*a):
        print("F", a, b)
        z = F(a, b)
        print("F", a, b, z)
        s += z
    return s

#assert F(3, 4) == 53
#assert F(9, 10) == 8152650
#assert G(3) == 72
print(sum(G(a) for a in range(2, 21)))
