# Brute force boys
def tri_search(n):
    r = 0
    for x1 in range(n+1):
        for y1 in range(n+1):
            if x1 == 0 and y1 == 0:
                continue
            asq = x1**2 + y1**2
            
            for x2 in range(x1, n+1):
                for y2 in range(y1+1):
                    if x2 == 0 and y2 == 0 or x1 == x2 and y1 == y2:
                        continue
                    
                    bsq = x2**2 + y2**2
                    csq = (x2 - x1)**2 + (y2 - y1)**2
                    
                    if asq + bsq == csq or asq + csq == bsq or bsq + csq == asq:                  
                        r += 1
                        
        print(x1, r)

    return r

    
print(tri_search(50))
