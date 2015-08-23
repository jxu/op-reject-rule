# Thanks Euclid
# sum = k(2m^2 + 2mn)
from fractions import gcd

L = 1500000
triangles = [0]*(L+1)
for m in range(1, int((L/2)**0.5) + 1):
    for n in range(m%2 + 1, m, 2):  # m-n odd; m,n > 0 
        s = 2*m**2 + 2*m*n
        if s > L:
            break
            
        if gcd(m, n) == 1:
            for k in range(1, int(L/s)+1):
                triangles[k*s] += 1
                
print(triangles.count(1))
