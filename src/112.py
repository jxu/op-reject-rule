def cmp(a, b):
    return (a > b) - (a < b)

def is_bouncy(n):
    sn = str(n)
    directions = [cmp(sn[i+1], sn[i]) for i in range(len(sn)-1)]
    return 1 in directions and -1 in directions


n = 0
for d in range(1, 10**8):
    if is_bouncy(d): n += 1
    if d % 1000 == 0: print(d, n/d)
    if n/d == 0.99:
        print(d, n/d)
        break