from functools import cache

rule7 = (1, 3, 2, -1, -3, -2)  # 10^n mod 7


def update_params(d_new, par, m7, m3, depth):
    # flip parity bit
    par_new = par ^ (1 << (d_new // 2))
    m3_new = (m3 + d_new) % 3
    m7_new = (m7 + rule7[depth % 6] * d_new) % 7
    return par_new, m3_new, m7_new

@cache
def f(d, par, m7, m3, depth):
    #print(d, "{:05b}".format(par), m7, m3, depth)
    if depth == 0:
        return int((d, par, m7, m3) == (5, 0b11111, 0, 0))
    s = 0
    for d_new in (1, 3, 5, 7, 9):
        par_new, m3_new, m7_new = update_params(d_new, par, m7, m3, depth)
        s += f(d_new, par_new, m7_new, m3_new, depth-1)
    return s

ODD = (1, 3, 5, 7, 9)

def search(n, d, par, m7, m3, depth):

    if depth == 0:
        return ""

    n_rem = n
    s = 0
    
    for d_new in (1, 3, 5, 7, 9):

        par_new, m3_new, m7_new = update_params(d_new, par, m7, m3, depth)
       
        node_sum = f(d_new, par_new, m7_new, m3_new, depth-1)
        print(n_rem, node_sum, d_new, par_new, m7_new, m3_new, depth-1)

        if n_rem - node_sum < 0:  # too far, use i only

            return str(d_new) + search(n_rem, d_new, par_new, m7_new, m3_new, depth-1)

        else:
            n_rem -= node_sum
            s += node_sum

    return s

#print(f(0, 0, 0, 0, 7))

def T(n):

    for depth in range(7, 30):
        r = search(n-1, 0, 0, 0, 0, depth)
        if type(r) == int:
            n -= r
        elif r:
            return r
    

print(T(10**16))       
