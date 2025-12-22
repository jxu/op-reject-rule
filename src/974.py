# Digit-by-digit DP
# TODO: use leading zeros to include smaller depths?

from functools import cache

# 10^n mod 7 = 1, 3, 2,-1,-3,-2, ... (period 6)
# 10^n mod 3 = 1, 1, 1, 1, 1, 1, ... (period 1)
RULE21 = (1, 10, 16, 13, 4, 19)  # 10^n mod 21, period 6

# Could try avoid storing param d by handling the last 5 as a special case
# But makes calc and search harder
@cache
def f(d, par, m21, depth):
    if depth == 0:
        return (d, par, m21) == (5, 0b11111, 0)
    
    s = 0
    # count leading zeros to simplify search
    for d_new in (0, 1, 3, 5, 7, 9):
        if d_new == 0:
            if d != 0: continue  # only can have 0 following 0
            par_new = par

        else:
            par_new = par ^ (1 << (d_new // 2))  # flip parity bit
            
        m21_new = (m21 + RULE21[depth % 6] * d_new) % 21
        
        s += f(d_new, par_new, m21_new, depth-1)
    
    return s

def search(n, d, par, m21, depth):

    if depth == 0:
        return ""
    
    for d_new in (0, 1, 3, 5, 7, 9):
        if d_new == 0:
            if d != 0: continue
            par_new = par
        else:
            par_new = par ^ (1 << (d_new // 2))
        
        m21_new = (m21 + RULE21[depth % 6] * d_new) % 21
 
        node_sum = f(d_new, par_new, m21_new, depth-1)
        #print(n_rem, node_sum, d_new, depth-1)

        if n - node_sum < 0:  # correct node to go down
            return str(d_new) + search(n, d_new, par_new, m21_new, depth-1)

        else:
            n -= node_sum



def T(n):
    return int(search(n-1, 0, 0, 0, 30))


print(T(10**16))       
