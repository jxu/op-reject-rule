# Easy peasy 
def N(n):
    t = [0]*(n+1)
    pad = 2
    while (1 + pad)**2 - 1 <= n:
        x = 1
        while (x + pad)**2 - x**2 <= n:
            t[(x + pad)**2 - x**2] += 1
            x += 1
                
        pad += 2
    return t
        
t = N(1000000)
print(sum(t.count(n) for n in range(1, 11)))
