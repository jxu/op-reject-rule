# 1st, 3rd, ... digits - 2nd, 4th, ... digits = 0 (mod 11)


# Turn 20! problem -> 10!
def gen_odd(current, remaining):
    #print(current, remaining)
    if len(current) == 10:
        # Current = odd, remaining = even 
        if (sum(current) - sum(remaining)) % 11 == 0: 
            print(current, sum(current) - sum(remaining))
            return 1
        return 0
    
    s = 0 # change
    for d in range(10):
        if d in remaining and (current == [] or d >= current[-1]):
            new_current = current + [d]
            new_remaining = remaining[:]
            new_remaining.remove(d)
            #print(new_current, new_remaining)
            s += gen_odd(new_current, new_remaining)
            
    return s

current = []
remaining = list(range(10))*2

print(gen_odd(current, remaining))
