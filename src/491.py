# 1st, 3rd, ... digits - 2nd, 4th, ... digits = 0 (mod 11)
import math

def combination(l): # Remove duplicate digits
    c = math.factorial(len(l))
    for n in set(l):
        c //= l.count(n)
        
    return c


def gen_odd(current, remaining):
    if len(current) == 10:
        # Current = odd, remaining = even 
        if (sum(current) - sum(remaining)) % 11 == 0: 
            #print(current, remaining)
            return combination(current) * combination(remaining)
        return 0
    
    s = 0 
    for d in range(10):
        if d in remaining and (current == [] or d >= current[-1]):
            new_remaining = remaining[:]
            new_remaining.remove(d)
            s += gen_odd(current + [d], new_remaining)
            
    return s


print(gen_odd([], list(range(10))*2) * 9//10) # 9/10 possible don't start with 0
