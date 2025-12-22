# Digit-by-digit DP
# TODO: use leading zeros to include smaller depths?

from functools import cache

# 10^n mod 7 = 1, 3, 2, -1, -3, -2, ... (period 6)
# 10^n mod 3 = 1, 1, 1, 1, 1, 1, ... (period 1)
RULE21 = (1, 10, 16, 13, 4, 19)  # 10^n mod 21, period 6

@cache
def f(d, par, m21, depth):
    if depth == 0:
        return int((d, par, m21) == (5, 0b11111, 0))
    
    s = 0
    for d_new in (1, 3, 5, 7, 9):
        par_new = par ^ (1 << (d_new // 2))  # flip parity bit
        m21_new = (m21 + RULE21[depth % 6] * d_new) % 21
        s += f(d_new, par_new, m21_new, depth-1)
    
    return s

def search(n, par, m21, depth):

    if depth == 0:
        return ""

    n_rem = n
    s = 0
    
    for d_new in (1, 3, 5, 7, 9):
        par_new = par ^ (1 << (d_new // 2))
        m21_new = (m21 + RULE21[depth % 6] * d_new) % 21
 
        node_sum = f(d_new, par_new, m21_new, depth-1)
        #print(n_rem, node_sum, d_new, depth-1)

        if n_rem - node_sum < 0:  # too far, use i only

            return str(d_new) + search(n_rem, par_new, m21_new, depth-1)

        else:
            n_rem -= node_sum
            s += node_sum

    return s


def T(n):

    for depth in range(7, 30):
        r = search(n-1, 0, 0, depth)
        if type(r) == int:
            n -= r
        elif r:
            return r
    

print(T(10**16))       
