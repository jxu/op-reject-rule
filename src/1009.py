from math import ceil, floor, log


# max is exclusive
def f(a, b, k, n_min, n_max, a_base=0, b_base=0):
    #print(k, n_min, n_max, a_base, b_base)

    if k == -1:
        print(f"end [{n_min},{n_max})")
        return n_max - 1

    res = 0

    for d in range(a):
        n_a_min = a_base + d * a**k
        n_a_max = n_a_min + a**k 

        n_b_min = ceil((b_base + d * b**k) / 2)
        n_b_max = ceil((b_base + (d+1) * b**k) / 2) 

        #print(d)
        #print(n_a_min, n_a_max, n_b_min, n_b_max)

        # restrict interval
        new_n_min = max(n_min, n_a_min, n_b_min)
        new_n_max = min(n_max, n_a_max, n_b_max)

        if new_n_max - new_n_min < 1:
            continue 

        res = max(res, f(a, b, k-1, new_n_min, new_n_max, a_base=n_a_min, b_base=(b_base + d * b**k)))

    return res


def F(a, b):
    max_k = int(log(4) / log(b / a))
    #print("max_k", max_k)
    return f(a, b, max_k, 1, a**(max_k+1))

def G(a):
    s = 0
    for b in range(a+1, 4*a):
        z = F(a, b)
        print("F", a, b, z)
        s += z
    return s

print(sum(G(a) for a in range(2, 21)))
