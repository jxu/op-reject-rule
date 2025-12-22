# Digit-by-digit DP
# Have to use DP because storing the entire digit string is impractical

# 1) Div by 105 <=> div by 3, 5, and 7
# Div by 5 is ensured by last digit being 5
# Div by 7 has no easy divisibility rule trick like 3 (add the digits mod),
# so we simply expand the number in base 10.

# 2) Odd digits is ensured by the DP branching, although leading zeros are
# used to simplify the depth search

# 3) Odd counts of odd digits are stored by 5 bits packed into one int

from functools import cache

# 10^n mod 7 = 1, 3, 2,-1,-3,-2, ... (period 6)
# 10^n mod 3 = 1, 1, 1, 1, 1, 1, ... (period 1)
RULE21 = (1, 10, 16, 13, 4, 19)  # 10^n mod 21, period 6

# Could try avoid storing param d by handling the last 5 as a special case
# but makes calc and search harder
# Since depth always recurses one level, could use a bottom-up loop by 
# increasing depth and overwrite the prev depth
@cache
def f(d, par, m21, depth):
    if depth == 0:
        return (d, par, m21) == (5, 0b11111, 0)
    
    s = 0
    # count leading zeros to simplify search
    for d_new in (0, 1, 3, 5, 7, 9):
        if d_new == 0 and d != 0: 
            continue # only can have 0 following 0
            
        # flip parity bit (if not zero)
        par_new = par ^ ((d_new != 0) * 1 << (d_new // 2))
        m21_new = (m21 + RULE21[depth % 6] * d_new) % 21
        
        s += f(d_new, par_new, m21_new, depth-1)
    
    return s

def search(n, d, par, m21, depth):
    if depth == 0:
        return ""
    
    for d_new in (0, 1, 3, 5, 7, 9):
        if d_new == 0 and d != 0: 
            continue # only can have 0 following 0
            
        par_new = par ^ ((d_new != 0) * 1 << (d_new // 2))
        m21_new = (m21 + RULE21[depth % 6] * d_new) % 21
        
        node_sum = f(d_new, par_new, m21_new, depth-1)
        print(n, node_sum, d_new, depth-1)

        if n <= node_sum:  # correct node to go down
            # build digit-by-digit, could just print digit
            return str(d_new) + search(n, d_new, par_new, m21_new, depth-1)

        n -= node_sum

    raise ValueError  # helps typecheck


def T(n):
    return int(search(n, 0, 0, 0, 30))


print(T(10**16))       
